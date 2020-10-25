from typing import Optional

import pandas as pd


class DFService:
    def swap_and_remove_path(
        self,
        df: pd.DataFrame,
        base_dir: Optional[str] = None
    ) -> pd.DataFrame:
        service = ImageDownloadService()

        for i, image_hashes in enumerate(df.image_hash):
            image_paths = []
            for image_hash in image_hashes:
                maybe_local_path = service.get_local_path(
                    image_hash=image_hash,
                    base_dir=base_dir
                )
                if maybe_local_path is None:
                    print("Skipped this data.")
                else:
                    image_paths.append(maybe_local_path)
            df.at[i, 'image_path'] = image_paths

        return df[df['image_path'].map(len) == df['num']]


class ImageDownloadService:
    def get_local_path(
        self,
        image_hash: str,
        base_dir: Optional[str]
    ) -> Optional[str]:
        return None
