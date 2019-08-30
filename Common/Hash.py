# -*- coding: utf-8 -*-
# @Time   :2019/08/13
# @Author    : chenyue
import hashlib
import binascii
from crypto.Cipher import AES
from crypto.Cipher import DES


def hash_md5(msg):
    """
    md5加密
    :param msg: 需要加密的字符串
    :return:  加密之后的字符串
    """
    h = hashlib.md5()
    h.update(msg.encode('utf-8'))
    return h.hexdigest()


def my_sha1(msg):
    """
    sha1加密
    :param msg:需要加密的字符串
    :return: 加密后的字符串
    """
    sh = hashlib.sha1()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()


def my_des(msg, key):
    """
    DES加密
    :param msg: 需要加密的字符串，长度必须是8的倍数，不足添加“=”
    :param key:8个字符
    :return:  加密后的字符串
    """
    de = DES.new(key, DES.MODE_ECB)
    mss = msg + (8-(len(msg) % 8)) * '='
    text = de.encrypt(mss.encode())
    return binascii.b2a_hex(text).decode()


def my_aes_encrypt(msg, key, vi):
    """
    AES加密
    :param msg: 需要加密的字符串
    :param key: 必须为16，24，32位
    :param vi:必须位16位
    :return:加密后的字符串
    """
    obj = AES.new(key, AES.MODE_CBC, vi)
    txt = obj.encrypt(msg.encode())
    return binascii.b2a_hex(txt).decode()


def my_aes_decrypt(msg, key, vi):
    """
    AES算法解密
    :param msg:需要解密的字符串
    :param key:必须为16，24，32位
    :param vi:必须为16位
    :return:解密后的字符串
    """
    msg = binascii.a2b_hex(msg)
    obj = AES.new(key, AES.MODE_CBC, vi)
    return obj.decrypt(msg).decode()



