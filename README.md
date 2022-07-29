# Data Analytics Platform

Has been inspired from a similar MediaCompSys project analyzing customer watch time data.

## Details

Project reads CSV file and validates parsed data. Constraints include name lengths, age number, and the use of special characters.
If the data is invalid, the data is sent through ActiveMQ along with an error message for further processing. Valid Data is sent to a MySQL Server for storage.

## Usage

```python
python -u ../..../csvProcess.py
```

![GitHub repo file count](https://img.shields.io/github/directory-file-count/wanderman12345/DAP)


![CODE!](Users/mathewraju/Downloads/carbon.png)

