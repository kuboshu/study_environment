# MySQLの練習環境
MySQLの使い方を勉強するための環境です。serverとclientの２つのコンテナで構成されており、データをserver側に登録してclient側からデータベースを操作します。


# 注意

- この環境はMySQLの操作を体験するためだけの使用を想定しており、パフォーマンスやセキュリティの事は一切考慮していませんので、勉強以外の目的で使用しないでください。

- ダウンロードしたデータの都合上、テーブルが１つしか無いため結合(join...)などの操作はできません。

- データの永続化はしていないので、コンテナ上で行った内容はコンテナ停止と共に削除されます。

# 使い方

## Docker composeで起動する。

説明する際のプロンプトは、ホスト側での操作の時は"host> "、serverコンテナ側では"server> "、clientコンテナ側では"client> "で表示してます。

### 0. データをダウンロードする
[UCI Machine Learning Repository(Student Performance)](https://archive.ics.uci.edu/ml/datasets/Student+Performance)からデータをダウンロードして、以下の２つのcsvファイルをcontents/に配置します。

- student-mat.csv
- student-por.csv

### 1. コンテナを起動する
```base
host> docker-compose up -d --build
```

### 2. クライアントに接続する
```base
host> docker exec -it mysql_client_1 bash
```

### 3. クライアントからサーバのMySQLに接続する。
```bash
client> mysql -hmysql_server_1 -uroot -proot
```
mysqlを起動するとプロンプトが以下の様にmysqlに変化します。

```bash
mysql> 
```

### 4. MySQLを操作
```bash
# 例) データベース一覧表示
mysql> show databases;
```

### 5. MySQLを終了
```bash
mysql> quit
```
mysqlを終了するとプロンプトがクライアントとシェルに変化します。
```bash
client>
```

### 6. クライアントサーバとの接続解除
```bash
client> exit
```

### 7. コンテナ停止
```bash
host> docker-compose down
```

# 勉強会のメンバーへ

- この環境を使って何か得られた知見(操作方法のコツ等)がありましたら、簡単でいいので共有してくれると助かります!!

- この環境に関して要望がありましたらご連絡いただければと思います。

# 参考
- [Dockerhub:Mysql](https://hub.docker.com/_/mysql)
- [UCI Machine Learning Repository(Student Performance)](https://archive.ics.uci.edu/ml/datasets/Student+Performance)