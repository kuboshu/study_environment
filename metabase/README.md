# Metabaseの練習環境
Metabaseの使い方を勉強するための環境です。metabaseサーバとmysqlサーバの２つのコンテナで構成されており、データをMySQL側に登録してMetabase側からデータベースを参照します。


# 注意

- この環境はMetabaseの操作を体験するためだけの使用を想定しており、パフォーマンスやセキュリティの事は一切考慮していませんので、勉強以外の目的で使用しないでください。

- データの永続化はしていないので、コンテナ上で行った内容はコンテナ停止と共に削除されます。

# 使い方

説明する際のプロンプトは、ホスト側での操作の時は"host> "、serverコンテナ側では"server> "、clientコンテナ側では"client> "で表示してます。

### 0. データをダウンロードする
[UCI Machine Learning Repository(Student Performance)](https://archive.ics.uci.edu/ml/datasets/Student+Performance)からデータをダウンロードして、以下のtxtファイルをcontents/に配置します。

- household_power_consumption.txt

配置しましたら、reform.pyを実行してデータファイル中の日付表示をMySQLが読み取れる形式に変換してください。
具体的な処理はreform.pyのコードを参照してください。

```bash
host> python reform.py #Python3.6以上での実行を想定しています。(作者環境は3.8.6)
```

### 1. コンテナを起動する
```base
host> docker-compose -d --build
```

### 2. Metabaseに接続する
```base
host> docker exec -it mysql_client_1 bash
```

### 3. Metabaseで色々試す
```bash
client> mysql -hmysql_server_1 -uroot -proot
```
mysqlを起動するとプロンプトが以下の様にmysqlに変化します。

```bash
mysql> 
```

### 7. コンテナ停止
```bash
host> docker-compose down
```

# 勉強会のメンバーへ

- この環境を使って何か得られた知見(操作方法のコツ等)がありましたら、簡単でいいので共有してくれると助かります!!

- この環境に関して要望がありましたらご連絡いただければと思います。

# 参考
- [Dockerhub:Metabase](https://hub.docker.com/_/mysql)
- [UCI Machine Learning Repository(Student Performance)](https://archive.ics.uci.edu/ml/datasets/Student+Performance)