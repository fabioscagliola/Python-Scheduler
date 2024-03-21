import asyncio
import logging
import time
import uuid

logging.basicConfig(level=logging.INFO, format='%(asctime)s — %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()


# Base class for activity parameters
class ActivityParameters:
    def __init__(self):
        pass


# Base class for activities
class Activity:
    def __init__(self, name, parameters, period):
        self.name = name
        self.parameters = parameters
        self.period = period  # The period of execution [seconds]
        self.id = uuid.uuid4()  # The correlation identifier

    async def execute(self):
        logger.info(f"[{self.id}] Executing activity \"{self.name}\"..")


# The parameters of an activity that computes a Fibonacci number
class NumbActivityParameters(ActivityParameters):
    def __init__(self, position, number=0):
        super().__init__()
        self.position = position  # The position of the Fibonacci number in the sequence
        self.number = number  # The Fibonacci number


# An activity that computes a Fibonacci number
class NumbActivity(Activity):
    async def execute(self):
        await super().execute()
        await asyncio.sleep(2)  # Simulate some asynchronous work
        self.parameters.number = self.fibonacci(self.parameters.position)
        logger.info(f"[{self.id}] Fibonacci number at position {self.parameters.position} is {self.parameters.number}")

    def fibonacci(self, number):
        if number > 1:
            return self.fibonacci(number - 1) + self.fibonacci(number - 2)
        return number


# The parameters of an activity that computes the MD5 hash of a string
class HashActivityParameters(ActivityParameters):
    def __init__(self, string, hash=""):
        super().__init__()
        self.string = string  # The input string
        self.hash = hash  # The output MD5 hash


# An activity that computes the MD5 hash of a string
class HashActivity(Activity):
    async def execute(self):
        await super().execute()
        await asyncio.sleep(3)  # Simulate some asynchronous work
        self.parameters.hash = self.md5(self.parameters.string)
        logger.info(f"[{self.id}] The MD5 hash of \"{self.parameters.string}\" is {self.parameters.hash}")

    def md5(self, string):
        import hashlib
        return hashlib.md5(string.encode()).hexdigest()


# An activity that throws an exception
class FoulActivity(Activity):
    async def execute(self):
        await super().execute()
        await asyncio.sleep(4)  # Simulate some asynchronous work
        raise Exception("May your knife chip and shatter")


async def schedule_activity(activity):
    while True:
        init_time = time.time()
        try:
            await activity.execute()
        except Exception as e:
            logger.error(f"[{activity.id}] Something went wrong while attempting to execute activity {activity.name}:")
            logger.error(f"[{activity.id}]   {e}")
        exec_time = time.time() - init_time
        wait_time = max(0, activity.period - exec_time)
        await asyncio.sleep(wait_time)


async def main():
    logger.info("Python Scheduler began.")
    logger.info("Press CTRL + C to quit.")
    foul = FoulActivity("Foul", None, 30)
    hash = HashActivity("Hash", HashActivityParameters("Lisan al-Gaib"), 20)
    numb = NumbActivity("Numb", NumbActivityParameters(9), 10)
    await asyncio.gather(
        schedule_activity(numb),
        schedule_activity(foul),
        schedule_activity(hash),
    )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Python Scheduler ended.")
