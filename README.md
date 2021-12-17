# delaunay-diagram

## プログラムについて
座標とその地点の温度が入ったデータを受け取り、ドロネー三角形分割を行って気温が高いエリアは赤色、低いエリアは青色で描画する。<br>

### get_Random2Dpoints
指定した個数の座標と温度（指定した範囲内）をランダムに発生させる。<br>
（本番はcsvファイルから読み込む)
### hsv_to_rgb
温度を元にhsvで表した色をrgbに変換する。
### get_color
三角形を作る3点の温度を元に色を計算する。<br>
hsvで表し、hsv_to_rgbでrgbに変換したものを返す。
### get_ave
三角形の色を計算するときに使う、すべての三角形の温度の平均値の平均値と標準偏差を計算する。
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
