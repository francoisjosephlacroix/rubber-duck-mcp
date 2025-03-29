import logging
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)

class RubberDuckTool:
    """A rubber duck debugging tool that receives code and context but doesn't respond."""
    
    async def process(self, code: str, context: Optional[str] = None) -> None:
        """
        Process the code and context received from the LLM.
        This is a one-way communication - we don't send anything back.
        
        Args:
            code: The code the LLM is trying to debug
            context: Optional context about the debugging situation
        """
        # Log the interaction
        timestamp = datetime.utcnow().isoformat()
        log_entry = {
            "timestamp": timestamp,
            "code": code,
            "context": context,
        }
        
        # Log to both file and console
        logger.info("Rubber Duck Session: %s", log_entry)
        
        # In a real implementation, you might want to:
        # 1. Store the session in a database
        # 2. Generate analytics
        # 3. Track debugging patterns
        # For now, we just log it 