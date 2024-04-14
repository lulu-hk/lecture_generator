
from graphviz import Digraph

syllabus = [
    {
        'week': 1,
        'topics': ['料理の基礎'],
        'lectures': [
            {'title': '料理の基本概念', 'description': '料理の基本的な概念について説明します。'},
            {'title': '包丁の使い方と切り方', 'description': '包丁の正しい使い方と基本的な切り方を教えます。'},
            {'title': 'だしの取り方と調味料の使い方', 'description': 'だしの取り方と基本的な調味料の使い方についてレクチャーします。'}
        ]
    },
    {
        'week': 2,
        'topics': ['和食料理の応用'],
        'lectures': [
            {'title': '料理の基本概念の復習', 'description': '1週目に学んだ料理の基本概念を復習します。'},
            {'title': '代表的な和食料理の作り方', 'description': '代表的な和食料理の作り方について深掘りして説明します。'},
            {'title': '盛り付けとテーブルセッティング', 'description': '美しい盛り付けのコツとテーブルセッティングについて学びます。'}
        ]
    },
    {
        'week': 3,
        'topics': ['フランス料理の基礎'],
        'lectures': [
            {'title': 'フランス料理の歴史と特徴', 'description': 'フランス料理の歴史や特徴の概要を説明します。'},
            {'title': '基本的なソースの作り方', 'description': 'フランス料理の基本的なソースの作り方を解説します。'},
            {'title': 'フルコースメニューの作成', 'description': '習得した技術を活かした実践的なフルコースメニューの作成方法を学びます。'}
        ]
    },
    {
        'week': 4,
        'topics': ['中華料理の基礎'],
        'lectures': [
            {'title': '中華料理の歴史と特徴', 'description': '中華料理の歴史や特徴について概説します。'},
            {'title': '基本的な調理法と食材の扱い方', 'description': '中華料理の基本的な調理法や食材の扱い方を解説します。'},
            {'title': '代表的な中華料理のレシピと調理法', 'description': '代表的な中華料理のレシピを紹介し、実践的な調理法を学びます。'}
        ]
    },
    {
        'week': 5,
        'topics': ['デザートの基礎'],
        'lectures': [
            {'title': 'デザートの歴史と種類', 'description': 'デザートの歴史や種類について概要を説明します。'},
            {'title': '基本的な製菓技術', 'description': 'ケーキ、タルト、プリンなど、代表的なデザートの作り方を実践的に学びます。'},
            {'title': 'デザートのプレゼンテーションとテーブルコーディネート', 'description': 'デザートのプレゼンテーションやテーブルコーディネートのコツについて学びます。'}
        ]
    }
]

g = Digraph(comment='Syllabus Graph')

for week_data in syllabus:
    week_index = week_data['week']
    week_topics = ', '.join(week_data['topics'])
    week_node_name = f"Week {week_index}\n{week_topics}"
    g.node(week_node_name, shape='box', style='filled', fillcolor='lightblue')
    
    with g.subgraph(name=f'cluster_week{week_index}') as c:
        lecture_titles = '\n'.join([lecture['title'] for lecture in week_data['lectures']])
        c.node(f'lectures_week{week_index}', shape='box', label=lecture_titles)
        g.edge(week_node_name, f'lectures_week{week_index}', style='dashed', tailport='s', headport='sw')

for i in range(len(syllabus) - 1):
    current_week_data = syllabus[i]
    next_week_data = syllabus[i + 1]
    current_week_node_name = f"Week {current_week_data['week']}\n{', '.join(current_week_data['topics'])}"
    next_week_node_name = f"Week {next_week_data['week']}\n{', '.join(next_week_data['topics'])}"
    g.edge(current_week_node_name, next_week_node_name)

g.render('syllabus_graph', view=True)
