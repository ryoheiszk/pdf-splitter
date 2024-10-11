# 指定ページ数ごとにPDF分割

```bash
python -m venv .venv

# Windowsの場合
source .venv/Scripts/activate

# Linuxの場合
source .venv/bin/activate

pip install -r requirements.txt
```

```bash
python main.py --input input.pdf --output output_prefix --split 60 <--start 50> <--end 200>
```
