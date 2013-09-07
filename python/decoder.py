class BinaryCode:

  def _decode(self, message, first = False):
    decoded_chain = [1 if first else 0]
    for i, c in enumerate(message[:-1]):
      if i == 0:
        last_num = 0
      else:
        last_num = int(decoded_chain[i-1])
      decoded = decoded_chain[i]
      encoded = int(c)
      original_val = encoded - (decoded + last_num)
      if original_val > 1 or original_val < 0:
        return None
      decoded_chain.append(original_val)
    return "".join(map(str, decoded_chain))

  def decode(self, message):
    return (self._decode(message) or "NONE", self._decode(message, True) or "NONE")

test = BinaryCode()
print test.decode("123210122")
print test.decode("11")
print test.decode("22111")
print test.decode("123210120")
print test.decode("3")
print test.decode("12221112222221112221111111112221111")
