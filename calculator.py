import logger
import logging

# Main calculator class
class Calculator:
    def add(self, a, b):
        logging.debug(f"Entering add() method with arguments: {a}, {b}")
        result = a + b
        logging.info(f"Adding {a} and {b}: {result}")
        logging.debug(f"Exiting add() method with result: {result}")
        return result

    def subtract(self, a, b):
        logging.debug(f"Entering subtract() method with arguments: {a}, {b}")
        result = a - b
        logging.info(f"Subtracting {a} from {b}: {result}")
        logging.debug(f"Exiting subtract() method with result: {result}")
        return result

    def multiply(self, a, b):
        logging.debug(f"Entering multiply() method with arguments: {a}, {b}")
        result = a * b
        logging.info(f"Multiplying {a} and {b}: {result}")
        logging.debug(f"Exiting multiply() method with result: {result}")
        return result

    def divide(self, a, b):
        logging.debug(f"Entering divide() method with arguments: {a}, {b}")
        if b == 0:
            logging.error(f"Division by zero error: {a}/{b}")
            return None
        elif b < 0.01:
            logging.warning(f"Dividing by a very small number: {b}, this might cause precision issues.")
        result = a / b
        logging.info(f"Dividing {a} by {b}: {result}")
        logging.debug(f"Exiting divide() method with result: {result}")
        return result

if __name__ == "__main__":
    logger.setup_logging()  # Initialize logging
    calc = Calculator()

    # Example operations
    calc.add(10, 5)
    calc.subtract(20, 4)
    calc.multiply(3, 7)
    calc.divide(10, 2)
    calc.divide(10, 0)
    calc.divide(10, 0.001)  # This will trigger a warning

    logging.critical("This is a critical message")