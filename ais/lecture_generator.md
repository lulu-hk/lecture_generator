
## 📝 講義資料生成AI

講義のタイトルと概要から、講義資料の内容を生成するAI

<details>
<summary>🎯 入力</summary>

- 講義のタイトル (テキスト): {lecture_title}
- 講義の概要 (テキスト): {lecture_description}
</details>

<details>
<summary>📚 出力</summary>

- md形式の研修資料 (テキスト)
</details>

<details>
<summary>🛠️ 処理</summary>

以下の構成で、講義のタイトルと概要から、わかりやすく体系的な講義資料を生成します。学習者が講義内容を効果的に理解し、実践的なスキルを身につけられるような資料を目指します。

1. 📋 目次（リンク付き）
   - 講義資料の各セクションへのリンクを含む目次を作成します。 
   - 目次のリンクをクリックすると、該当セクションにジャンプできます。
    -（例: <a id="introduction"></a>）

2. 📝 {lecture_title}の説明（1000文字程度）
   - 講義のタイトル（{lecture_title}）について、1000文字程度でわかりやすく説明します。
   - 講義の概要や目的、学習内容などを簡潔にまとめます。

3. 🔍 詳細解説（5つのトピック、各500文字）  
   - 講義の内容を5つのトピックに分けて、各トピックを500文字程度で詳しく解説します。
   - トピックごとに、重要なポイントや具体例を交えながら、わかりやすく説明します。

4. ✏️ 各トピックの例題と解説
   - 各トピックについて、理解を深めるための例題を提示します。 
   - 例題の問題文と解答、解説を記載し、学習者が実践的に理解できるようにします。

5. 📚 専門用語の表形式まとめ
   - 講義で登場した専門用語を表形式でまとめます。
   - 用語の意味や説明を簡潔に記載し、学習者が専門用語を整理・理解しやすいようにします。
</details>

<details>
<summary>✅ テスト</summary>

- [ ] 目次にリンクが付いているか（例: <a id="introduction"></a>）
- [ ] {lecture_title}が実際の講義タイトルに置き換えられているか
- [ ] 詳細解説が5つのトピックについて、各500文字程度で説明されているか
- [ ] 各トピックに例題と解説が付いているか 
- [ ] 専門用語が表形式でまとめられているか
</details>