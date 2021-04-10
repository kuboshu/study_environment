# Fessの実験用環境


# ローカルファイルシステムのクローリング

# Webのクローリング

# Gitbucketのクローリング

## ＜起動＞
```
host> docker-compose -f docker-compose.yml -f docker-compose.gitbucket.yml up -d --build
```

## ＜状態確認＞
```
host> docker-compose -f docker-compose.yml -f docker-compose.gitbucket.yml ps 
```

## ＜停止＞
```
host> docker-compose -f docker-compose.yml -f docker-compose.gitbucket.yml down
```

## ＜設定(Gitbucket側)＞
"localhost:28080"のURLにブラウザでアクセスして管理者(root)としてログインしてください。<br>
DockerのGitbucketであれば、初期パスワードは"root"となっています。<br>
<br>
![gitbucket_top](./figures/gitbucket_top.png)

### <u>Fess関連のプラグインをインストール</u>
[ここ](https://mvnrepository.com/artifact/org.codelibs.gitbucket/gitbucket-fess-plugin_2.13/1.7.0)からgitbucket-fess-plugin_2.13-1.7.0.jarをダウンロードして./contents/gitbucket_volume/plugins/にコピーしてください。<br>
コピーしたらGitbucketの管理画面からプラグインをリロードしてください。<br>
<br>
![gitbucket_plugin_before](./figures/gitbucket_plugin_before.png)
<br>
正常にロードできたら新しい項目が追加されます。<br>

![gitbucket_plugin_after](./figures/gitbucket_plugin_after.png)

### <u>トークンの発行</u>
FessからGitbucketにアクセスするためにトークンが必要なので生成します。<br>
管理ユーザで"Account Settings -> Applications"から説明を記載してトークン生成します。<br>
生成したトークンは一度しか表示されず、画面を切り替えると二度と確認できなくなるので注意してください。<br>

![gitbuket_gen_token](./figures/gitbucket_gen_token.png)


### <u>リポジトリの作成</u>
クローリングのテスト用に適当なリポジトリを作成してください。

## 設定(Fess側)
"localhost:18080"のURLにブラウザでアクセスして管理者(admin)としてログインしてください。<br>
DockerのFessであれば、初期パスワードは"admin"となっています。
なお、初回ログイン時にパスワードの変更を求められます。<br>
<br>
![fess_home](./figures/fess_top.png)

### ＜Gitbucket関連のプラグインをインストール＞
管理画面からGitbucketを使用するためのプラグインを導入します。<br>
図の様にプルダウンから"fess-ds-gitbucket-13.10.0"を選択してインストールしてください。<br>
<br>
![fess_plugin](./figures/fess_plugin.png)
<br>
正常にインストールできたら以下の様に追加されています。ここでGitbucketで生成したトークンを使用します。<br>

![fess_plugin_after](./figures/fess_plugin_after.png)

### ＜データストアのクローラ設定＞
クローリングの設定を行います。データストアを選択して新規作成から作成します。<br>
<br>
![fess_crawler_datastore](./figures/fess_crawler_datastore.png)
<br>
下図のように設定してください。<br>

![fess_crawler](./figures/fess_crawler.png)

### ＜ジョブの作成＞
![fess_crawler_after](./figures/fess_crawler_after.png)
<br>
"新しいジョブの作成"からジョブを作成してください。作成する際は全ての設定は初期のままで大丈夫です。<br>

![fess_create_job](./figures/fess_create_job.png)


### ＜ジョブの実行＞
"システム -> スケジューラ"から作成したジョブを選択して実行してください。<br>
<br>
![fess_scheduler_list](./figures/fess_scheduler_list.png)

### ＜結果の確認＞
正常にクローリングができていれば以下の様に検索結果が表示されます。<br>
<br>
![fess_search_result](./figures/fess_search_result.png)