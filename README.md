# delaunay-diagram
最新バージョンはdelaunay2.py
## プログラムについて
座標とその地点の温度が入ったデータを受け取り、ドロネー三角形分割を行って気温が高いエリアは赤色、低いエリアは青色で描画する。<br>


### get_color
三角形を作る3点の温度を元に色を計算する。<br>
hsvで表し、hsv_to_rgbでrgbに変換したものを返す。

### DelaunayDiagram
ドロネー三角形分割を行う。
### main
指定した大きさで、指定した点の数のドロネー三角形分割を行った画像を出力する。

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
