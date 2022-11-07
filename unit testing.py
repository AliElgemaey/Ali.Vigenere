import unittest

from CODEMAIN import encrypt

from CODEMAIN import decrypt


class Test(unittest.TestCase):

    def test_encryption(self):
        self.assertEqual(encrypt("Hello User", "sQLBs"), "ZUWMGq4$FJ")


    def test_decryption(self):
        self.assertEqual(decrypt("ZUWMGq4$FJ", "sQLBs"), "Hello User")

    def file_encrypt(self):
        encrypt_file = open("encrypt.txt", "r+")
        readplain = encrypt_file.read()
        decrypted = open("decryptedfile.txt", "r+")
        readdecrypted = decrypted.read()
        self.assertEqual(readplain, readdecrypted)
if __name__ == '__main__':
    unittest.main()