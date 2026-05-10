import requests
import uuid
import threading

class ImageDownloader(threading.Thread):
    def __init__(self, url):
        self.url = url
        threading.Thread.__init__(self)

    def run(self):
        image = requests.get(self.url).content
        image_name = f"images/{uuid.uuid4()}.jpg"
        with open(image_name, "wb") as f:
            f.write(image)
            print(f"Image downloaded and saved as {image_name}")


urls = [
    "https://images.unsplash.com/photo-1506744038136-46273834bf58",
    "https://images.unsplash.com/photo-1506744038136-46273834bf58",
    "https://images.unsplash.com/photo-1506744038136-46273834bf58"
]

threads = []

for url in urls:
    thread = ImageDownloader(url)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
