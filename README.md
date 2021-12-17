# delaunay-diagram

## コードを更新する手順
（※あってる自信ないけど！）
1. ローカルリポジトリでmasterブランチに入り、更新がないか確認<br>
  git checkout master<br>
  git pull<br>
  
2. 開発用ブランチに入る<br>
  git checkout ブランチ名<br>
  git branch で今のブランチを確認できる<br>
  
3. コード更新<br>

4. 変更点をローカルリポジトリでコミットする<br>
  git add .<br>
  git commit -m "変更点を書く"<br>
  
5. リポートリポジトリへpush<br>
  git push origin 開発用ブランチ名<br>
  
6. masterブランチに移動<br>
  git checkout master
8. リモートからマージしたファイルを取得<br>
  git pull origin ブランチ名
