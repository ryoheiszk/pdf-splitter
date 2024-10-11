# 指定ページ数ごとにPDF分割

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

```bash
python main.py --input input.pdf --output output_prefix --split 60 <--start 50> <--end 200>
```
