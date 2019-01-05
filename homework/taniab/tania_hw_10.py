import requests
import os


class ImageDownloader:
    _valid_image_types = ('png', 'jpg', 'jpeg')

    def __init__(self, urls_list, size_limit, target_folder=None):
        self.urls_list = urls_list
        self.size_limit = size_limit
        self.target_folder = target_folder or os.path.expanduser("~")

    def _validate_response(self, resp):
        if resp.status_code == 200:
            return True
        print(f'Requested image cannot be downloaded: {resp.status_code} - {resp.reason}')
        return False

    def _validate_type(self, resp):
        image_type = resp.headers['content-type'].split('/')[1]

        if image_type in self._valid_image_types:
            return True
        print(f'Image has invalid type {image_type}. Allowed types: {", ".join(self._valid_image_types)}')
        return False

    def _validate_size(self, resp):
        resp_size_kb = int(resp.headers['content-length']) / 1024

        if resp_size_kb <= self.size_limit:
            return True
        print(f'Image size is too large. Should be up to {self.size_limit} kb')
        return False

    def _save(self, resp):
        img_name = resp.url.split('/')[-1]
        path = os.path.join(self.target_folder, img_name)
        with open(path, 'wb') as img_file:
            for chunk in resp.iter_content(chunk_size=64):
                img_file.write(chunk)
        print(f'Successfully downloaded as {path}')

    def download_all(self):
        failed_urls = []
        for url in self.urls_list:
            response = requests.get(url)
            if all((self._validate_response(response), self._validate_size(response), self._validate_type(response))):
                self._save(response)
            else:
                failed_urls.append(url)

        if failed_urls:
            print(f'Failed to download:\n', '\n'.join(failed_urls))


downloader = ImageDownloader(['https://cs9.pikabu.ru/post_img/big/2018/08/21/6/1534844899115897608.jpg',
                              'https://www.pbs.org/wgbh/nova/media/original_images/quantum-entanglement_2048x1152.jpg',
                              'https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2018/04/space_rocks_live_cover/17465605-1-eng-GB/space_rocks_live_cover_large.jpg',
                              ], 900)
downloader.download_all()

