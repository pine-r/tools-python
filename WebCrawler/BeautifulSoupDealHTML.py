# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2020/11/17 22:55'
import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        return "获取HTML页面失败"


if __name__ == "__main__":
    url = "https://python123.io/ws/demo.html"
    demo = get_html(url)
    soup = BeautifulSoup(demo, "html.parser")    # 解释器html.parse
    print(soup.title)  # 打印html页面的title信息
    # 标签树的下行遍历
    print("head子节点信息：", soup.head.contents)
    print("body 子节点信息：", soup.body.contents)
    print("body 子节点信息的第二个元素：", soup.body.contents[1])
    for child in soup.body.children:
        print("遍历儿子节点", child)
    for child in soup.body.descendants:
        print("遍历子孙节点：", child)

    # 标签树的上行遍历
    print("head 标签父节点", soup.head.parent)
    for parent in soup.head.parents:
        if parent is None:
            print(parent)
        else:
            print("head 上行遍历：", parent.name)

    # 标签树的平行遍历
    print("a标签的后一个平行标签: ", soup.a.next_sibling)
    print("a标签的前一个平行标签: ", soup.a.previous_sibling)
    for sibling in soup.a.next_siblings:
        print("遍历后续节点：", sibling)

    for sibling in soup.a.previous_siblings:
        print("遍历前续节点：", sibling)

   # 获取标签
    tag = soup.a  # 打印出所有的a标签中第一个
    print("第一个a标签中的内容：", tag)
    a_name = soup.a.name  # a标签的名字
    print("a标签的名字:", a_name)
    a_parent_name = soup.a.parent.name  # a的父节点的名字
    print("a的父节点的名字:", a_parent_name)
    print("a的父节点的父节点的名字：", soup.a.parent.parent.name)

    # 获取标签属性
    print("a标签的属性：", tag.attrs)
    print("a的class属性的值：", tag.attrs['class'])
    print("a标签属性类型：", type(tag.attrs))
    print("a标签类型：", type(tag))

    # 获取标签内容
    print("a标签的内容：", tag.string)
    print("a标签的内容类型：", type(tag.string))

    # 处理标签注释, 和获取标签内容方法一样，只是type类型为<class 'bs4.element.Comment'>

    print(soup.prettify())
