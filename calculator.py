import logger
import logging
class Calculator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def add(self, a, b):
        result = a + b
        logging.debug(f"[DEBUG] Performing addition operation with {a} and {b}")
        logging.info(f"[INFO] Addition performed: {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        logging.debug(f"[DEBUG] Performing subtraction operation with {a} and {b}")
        logging.info(f"[INFO] Subtraction performed: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        logging.debug(f"[DEBUG] Performing multiplication operation with {a} and {b}")
        logging.info(f"[INFO] Multiplication performed: {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            logging.error(f"[ERROR] Division by zero attempted")
            return None
        elif b < 0.01:
            logging.warning(f"[WARNING] Attempting division with very small number ({b})")
        
        result = a / b
        logging.debug(f"[DEBUG] Performing division operation with {a} and {b}")
        logging.info(f"[INFO] Division performed: {a} / {b} = {result}")
        logging.warning("ok do it")
        return result

if __name__ == "__main__":
    logger.setup_logging()
    calc = Calculator()
    
    # Test to generate different log levels
    print("\nPerforming calculations...")
    calc.add(10, 5)
    calc.subtract(20, 4)
    calc.multiply(3, 7)
    calc.divide(10, 2)
    calc.divide(10, 0)  # This will generate an error log
    calc.divide(10, 0.001)  # This will generate a warning log
    logging.critical("[CRITICAL] Critical system event occurred")