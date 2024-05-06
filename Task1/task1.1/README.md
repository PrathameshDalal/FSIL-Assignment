# FSIL-Assignment Task 1.1: Downloading the 10K filings from SEC-EDGAR

## Installing SEC-EDGAR-DOWNLOADER

```python
pip install sec-edgar-downloader
```
## Downloading the 10K Filings using the sec-edgar-downloader for period 1995-2023

```python
# Creating a Downloader Object by passing in the 'company name', 'gmail' and 'path/to/save/location'
D1 = Downloader("prathamesh", "prathameshdalal100@gmail.com", ".")
# Downloading the 10-K filings using GET Method
D1.get("10-K", "AAPL", after="1994-12-31", before="2024-01-01")
D1.get("10-K", "MSFT", after="1994-12-31", before="2024-01-01")
D1.get("10-K", "BANF", after="1994-12-31", before="2024-01-01")
```
## Creating a Script to Download 10K filings automatically

```python
def get10Kfilings(name, email, path, companyname):
  d = Downloader(name, email, path)
  return d.get("10-K", companyname, after="1994-12-31", before="2024-01-01")
```

**Useage**

```python
get10Kfilings("JHON", "jhondoe@gmail.com", ".", "F")
```
