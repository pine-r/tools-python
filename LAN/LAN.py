# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2020/12/29 21:45'
"""
function: 判断两个IP是否是同一局域网
version: 1.0
原理： 如果两个IP的网络标识是一样的，则这两个IP属于同一局域网
"""
from flask import render_template
from flask import request
from LAN import LAN_blue


def decimal_to_binary(decimal):
    """
    将一个十进制数转换为二进制数
    :param decimal: 十进制数
    :return: 十进制数转换为二进制的01字符串
    """
    tmp = list()
    while decimal != 0:
        tmp.append(decimal % 2)
        decimal = decimal // 2
    tmp.reverse()
    res = "".join([str(num) for num in tmp])
    if len(res) < 8:
        res = "".join([("0" * (8 - len(res))), res])
    return res


def bitwise_and(str1, str2):
    """
    将两个01字符串按位与，例如11110000 & 11111111 = 11110000
    :param str1: 11110000
    :param str2: 11111111
    :return: 11110000
    """
    # 按位与存到临时变量tmp
    tmp = list(map(lambda x, y: int(x) and int(y), str1, str2))
    # 将整数数组转换为字符数组
    res = [str(x) for x in tmp]
    return "".join(res)


def bitwise_negation(my_string, x, y):
    """
    字符串按位取反，比如10101010，取反之后为01010101
    :param my_string: 原始字符串，例如10101010
    :param x: 字符，1
    :param y: 字符，2
    :return: 返回取反之后的字符串，例如：01010101
    """
    return my_string.replace(x, "tmp").replace(y, x).replace("tmp", y)


def deal_address_and_mask(address, mask):
    """
    返回IP地址和掩码转换为二进制之后的值
    :param address: IPV4地址
    :param mask: 掩码
    :return: ip_address_to_bin， subnet_mask_to_bin
    """
    ip_address_to_bin = list()
    subnet_mask_to_bin = list()
    for i in address.split('.'):  # 将IP地址分割，每一位进行二进制转换
        # print("IP 地址{0}".format(i))
        # print("IP 二进制{0}".format(decimal_to_binary(int(i))))
        ip_address_to_bin.append(decimal_to_binary(int(i)))
    for i in mask.split('.'):
        # print("掩码{0}".format(i))
        # print("掩码 二进制{0}".format(decimal_to_binary(int(i))))
        subnet_mask_to_bin.append(decimal_to_binary(int(i)))
    return ip_address_to_bin, subnet_mask_to_bin


@LAN_blue.route('/lan_index')
def lan_index():
    return render_template('LAN/LAN_index.html')


@LAN_blue.route('/judge_lan', methods=['GET', 'POST'])
def judge_lan():
    if request.method == "POST":
        # 获取IP1地址和掩码并解析: 将地址和掩码分别用点号分割，一个一个进行二进制转换，保存到数组中
        ip_address1 = request.form['ip_address1']
        print("输入的IP地址1：{0}".format(ip_address1))
        subnet_mask1 = request.form['subnet_mask1']
        print("输入的掩码1：{0}".format(subnet_mask1))
        ip_address1_to_bin, subnet_mask1_to_bin = deal_address_and_mask(ip_address1, subnet_mask1)
        print("IP地址1转换为二进制：{0}".format(ip_address1_to_bin))
        print("掩码1转换为二进制：{0}".format(subnet_mask1_to_bin))

        # 求IPV4地址1的网络标识
        address1_net_id = list()
        for i in range(0, 4):
            print("ip {0} and mask {1} : {2}".format(ip_address1_to_bin[i], subnet_mask1_to_bin[i], bitwise_and(ip_address1_to_bin[i], subnet_mask1_to_bin[i])))
            address1_net_id.append(bitwise_and(ip_address1_to_bin[i], subnet_mask1_to_bin[i]))
        print("网络标识{0}".format(address1_net_id))

        # 求IP1主机标识: ip & 掩码取反
        print("子网掩码1{0}".format(subnet_mask1_to_bin))
        subnet_mask1_reverse = list()
        for ele in subnet_mask1_to_bin:
            subnet_mask1_reverse.append(bitwise_negation(ele, "1", "0"))
        print("子网掩码1取反{0}".format(subnet_mask1_reverse))
        host1_id = list()    # 主机标识
        for i in range(0, 4):
            host1_id.append(bitwise_and(ip_address1_to_bin[i], subnet_mask1_reverse[i]))
        print("主机1标识{0}".format(host1_id))

        # 获取IP2地址和掩码并解析：将地址和掩码分别用点号分割，一个一个进行二进制转换，保存到数组中
        ip_address2 = request.form['ip_address2']
        subnet_mask2 = request.form['subnet_mask2']
        ip_address2_to_bin, subnet_mask2_to_bin = deal_address_and_mask(ip_address2, subnet_mask2)
        # 求IPV4地址2的网络标识
        address2_net_id = list()
        for i in range(0, 4):
            address2_net_id.append(bitwise_and(ip_address2_to_bin[i], subnet_mask2_to_bin[i]))
        # 求IP2主机标识
        subnet_mask2_reverse = list()
        for ele in subnet_mask2_to_bin:
            subnet_mask2_reverse.append(bitwise_negation(ele, "1", "0"))
        print("子网掩码2取反{0}".format(subnet_mask1_reverse))
        host2_id = list()  # 主机标识
        for i in range(0, 4):
            host2_id.append(bitwise_and(ip_address2_to_bin[i], subnet_mask2_reverse[i]))
        print("主机2标识{0}".format(host2_id))

        msg = "是同一局域网"
        if address1_net_id == address2_net_id:
            msg = "网络标识一样，是同一局域网！"
        else:
            msg = "网络标识不一样，不是同一局域网！"

        return render_template('LAN/LAN_index.html', ip_address1=ip_address1, subnet_mask1=subnet_mask1,
                               ip_address1_to_bin=ip_address1_to_bin, address1_net_id=address1_net_id, host1_id=host1_id,
                               ip_address2=ip_address2, subnet_mask2=subnet_mask2, host2_id=host2_id,
                               ip_address2_to_bin=ip_address2_to_bin, address2_net_id=address2_net_id,
                               subnet_mask1_to_bin=subnet_mask1_to_bin, subnet_mask2_to_bin=subnet_mask2_to_bin, msg=msg)


if __name__ == "__main__":
    # print(decimal_to_binary(253))
    pass
