byteData = bytearray()

with open("Secret.log:EvenMoreSecret", "rb") as alternateDataStreamStream:
    byteData = alternateDataStreamStream.read()
    alternateDataStreamStream.close()

with open("EvenMoreSecret.exe", "wb") as outputStream:
    outputStream.write(byteData)
    outputStream.close()