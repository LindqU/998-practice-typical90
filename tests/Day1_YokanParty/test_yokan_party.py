"""hogehoge"""
import pytest
from task.Day1_YokanParty.yokan_party import main
from utility.mock_std import In, Out


def test_case1(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("tests/Day1_YokanParty/input/input1.txt")
    stdout: object = Out("tests/Day1_YokanParty/output/output1.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    main()
    assert stdout.outputs == stdout.validation


def test_case2(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("tests/Day1_YokanParty/input/input2.txt")
    stdout: object = Out("tests/Day1_YokanParty/output/output2.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    main()
    assert stdout.outputs == stdout.validation


def test_case3(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("tests/Day1_YokanParty/input/input3.txt")
    stdout: object = Out("tests/Day1_YokanParty/output/output3.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    main()
    assert stdout.outputs == stdout.validation
