import random
import string
class Base:
      @staticmethod
      def random_string():
          chars = string.ascii_letters + string.digits
          return "".join(random.choice(chars) for x in range(random.randint(8, 16)))
