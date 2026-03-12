import io
from fastapi.responses import StreamingResponse
from fastapi import FastAPI, File, HTTPException, UploadFile, responses
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
import logging
from predict import predict_churn, process_batch, predict_batch  # ty:ignore[unresolved-import]
from models import PredictionRequest, PredictionResponse  # ty:ignore[unresolved-import]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up...")
    yield
    logger.info("Closing down..")

app = FastAPI(
    title="Model deployment with FastAPI",
    description="",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,  # ty:ignore[invalid-argument-type]
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root() -> responses.RedirectResponse:  # ty:ignore[invalid-return-type]
    """Redirect to /docs"""
    try:
        logger.info("Redirecting to /docs")
        return responses.RedirectResponse("/docs")
    except Exception as e:
        logger.error(f"Error redirecting to /docs: {e}")
    
@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    """Make a prediction using the pre-trained model."""
    try:
        logger.info("Received prediction request")
        response = predict_churn(request)
        logger.info("Prediction successful ")
        return response
    except Exception as e:
        logger.error(f"Error during prediction : {e}")
        raise e
@app.post("/predict/batch")
async def predict_batch_endpoint(file: UploadFile = File(...)):
    
    if file.filename is None or not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="File must be a CSV")
    
    file_bytes = await file.read()

    # read and process the batch file
    input_df = process_batch(file_bytes)

    # make predictions
    responses = predict_batch(input_df)

    # prepare CSV output
    output = io.StringIO()
    responses.to_csv(output, index=False)
    output.seek(0)

    # Step 4: Return as downloadable CSV
    response = StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv"
    )
    response.headers["Content-Disposition"] = f"attachment; filename=predicted_{file.filename}"
    return response



