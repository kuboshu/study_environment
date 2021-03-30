# Seleniumの練習環境
Seleniumの使い方を勉強するための環境で、以下の2つのコンテナで構成されています。<br>

### 構成(サービス名)

- selenium: ブラウザとそのドライバ、およびリモートウェブドライバで構成されているコンテナです。<br>
  ホスト側のプログラムからこのコンテナのリモートウェブドライバに接続してブラウザを操作します。
- web: nginxのコンテナで、seleniumの接続ターゲットです。<br>
  ただし、webのコンテンツは作成していないのでやれる事は少ないです。<br>

nginxにwebコンテンツを作成する事で色々できるようになりますが、その場合nginxのファイルの永続化をしてください。
でないと、作成したコンテンツがコンテナの停止とともに消えてしまいます。

# 注意

- この環境はSeleniumの操作を体験するためだけの使用を想定しており、パフォーマンスやセキュリティの事は一切考慮していませんので、勉強以外の目的で使用しないでください。

- データの永続化はしていないので、コンテナ上で行った内容はコンテナ停止と共に削除されます。

# 使い方

説明する際のプロンプトは、ホスト側での操作の時は"host> "になっています。

### 1. コンテナを起動する
```base
host> docker-compose -d --build
```

### 2. ホスト側でJupyter-notebookを起動してコードを実行する。

sample/にサンプルプログラムを用意してありますので、コードの簡単な書き方はサンプルを参照してください。<br>
seleniumへの接続はcommand_executorにhttp://localhost:4444/wd/hub(seleniumのコンテナ)を指定してください。

```python
...
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options
)
...
```


### 4. コンテナ停止
Jupyter-notebookの使用が終了したら、コンテナを停止してブラウザを閉じてください。
```bash
host> docker-compose down
```

# 勉強会のメンバーへ

- この環境を使って何か得られた知見(操作方法のコツ等)がありましたら、簡単でいいので共有してくれると助かります!!

- この環境に関して要望がありましたらご連絡いただければと思います。


# 参考
- [Selenium:Docker](https://github.com/SeleniumHQ/docker-selenium)
- [Selenium:公式ページ](https://www.selenium.dev/)
- [web driver api](https://selenium-python.readthedocs.io/api.html)