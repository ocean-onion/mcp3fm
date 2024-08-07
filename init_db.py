from app import create_app, db
from app.models import User, Plugin  # Assuming these models exist
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = create_app()

with app.app_context():
    try:
        db.create_all()
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
