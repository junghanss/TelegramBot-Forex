# Price Notification Telegram Bot 
Telegram Bot with daily automated notifications for the USD price in Argentina.

## Requirements
* Telegram Bot API
* Python 3
* AWS CLI
* Serverless framework CLI

## Usage

Add your Telegram token and chat id in ```.env``` file.

Install Python dependencies using ```pipenv```:
```python
pipenv install
```
Install Serverless Python Requirements plugin:

```python
sls plugin install -n serverless-python-requirements
```
Deploy the lambda function using Serverless CLI:

```python
sls deploy -v
```
After deployment, the function will be triggered by CloudWatch Event everyday at 8am UTC. It can also be invoked manually using:
```python
sls invoke -f send_price
```
