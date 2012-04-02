import random
import string
class Base:
      def random_string(self):
          chars = string.ascii_letters + string.digits
          return "".join(random.choice(chars) for x in range(random.randint(8, 16)))
