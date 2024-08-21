import logging
import os
import sys
import pytest
import json
from pathlib import Path

logger = logging.getLogger(__name__)


class TestLipSync:
    """
    Test lip sync component
    """

    def test_lip_sync(self) -> None:
        from run_compute_syncnet_score_videos import get_conscent_video_verification_info

        input_video_path1 = Path(__file__).parent.parent / "input" / "lipsync_test" / "LipSyncScore1Example.mp4"
        get_conscent_video_verification_info(video_path=input_video_path1, output_json_path="./output1.json")
        assert os.path.isfile("./output1.json")

        with open("./output1.json", "r") as f:
            data = json.load(f)
            assert data["minDist"] < 7.8

        input_video_path2 = Path(__file__).parent.parent / "input" / "lipsync_test" / "LipSyncScore2Example.mp4"
        get_conscent_video_verification_info(video_path=input_video_path2, output_json_path="./output2.json")
        assert os.path.isfile("./output2.json")

        with open("./output2.json", "r") as f:
            data = json.load(f)
            assert data["minDist"] >= 7.8
