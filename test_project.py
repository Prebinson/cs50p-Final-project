from project import new_task, update_progress, pending_task, failed_tasked
import pytest
import csv
import datetime as dt

task='Sql'
goal="To do it"
progress="Start"
date=dt.datetime(2008,12,12)

def test_new_task(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    new_task(task,date,goal)
    with open("task.csv", mode="r", newline="") as fi :
        file=list(csv.reader(fi))
    assert file[0]== ["Task","Goal","Progress","Time"]
    assert file[1]== ["Sql","To do it","Pending","12/12/2008"]
def test_update_progress(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    new_task(task,date,goal)
    monkeypatch.setattr("builtins.input", lambda _: "2")
    update_progress(1)
    with open("task.csv",mode="r", newline="") as fi:
        file=list(csv.reader(fi))
    assert file[0]== ["Task","Goal","Progress","Time"]
    assert file[1]== ["Sql","To do it","Quarter","12/12/2008"]
def test_pending_task(tmp_path, monkeypatch,capsys):
    monkeypatch.chdir(tmp_path)
    new_task(task,date,goal)
    new_task("Python",dt.datetime(2008,11,11),"to learn it")
    monkeypatch.setattr("builtins.input", lambda _: "6")
    update_progress(1)
    monkeypatch.setattr("builtins.input", lambda _: "2")
    update_progress(2)
    pending_task()
    capture = capsys.readouterr().out
    assert "Python" in capture
    assert "Sql" not in capture
def test_failed_tasked(tmp_path, monkeypatch,capsys):
    monkeypatch.chdir(tmp_path)
    new_task(task,date,goal)
    new_task("Python",dt.datetime(2008,11,11),"to learn it")
    monkeypatch.setattr("builtins.input", lambda _: "7")
    update_progress(1)
    monkeypatch.setattr("builtins.input", lambda _: "2")
    update_progress(2)
    failed_tasked()
    capture = capsys.readouterr().out
    assert "Sql" in capture
    assert "Python" not in capture



