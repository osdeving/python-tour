# Logs estruturados
import structlog
logger = structlog.get_logger()
logger.info("mensagem", user="Ana", action="login")
# pip install structlog
