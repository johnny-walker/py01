{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "divided-museum",
   "metadata": {},
   "outputs": [],
   "source": [
    "#https://www.brilliantcode.net/1062/numpy-tutorial-basic-operations/\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "downtown-parking",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a=>[6 7 8 9]\n",
      "b=>[0 1 2 3]\n",
      "c=>[6 6 6 6]\n",
      "\n",
      "同加、同減一個數值:\n",
      "a=>[11 12 13 14]\n",
      "b=>[-5 -4 -3 -2]\n",
      "\n",
      "次方：\n",
      "d=>[25 16  9  4]\n"
     ]
    }
   ],
   "source": [
    "#維度相同的矩陣相加減\n",
    "\n",
    "# 維度相同的矩陣相加、減\n",
    "a = np.array( [6, 7, 8, 9] )\n",
    "b = np.arange( 4 )\n",
    "c = a - b\n",
    "print(\"a=>{0}\".format(a))\n",
    "print(\"b=>{0}\".format(b))\n",
    "print(\"c=>{0}\".format(c))\n",
    " \n",
    " \n",
    "print('\\n同加、同減一個數值:')\n",
    "# 同加、同減一個數值\n",
    "a += 5\n",
    "print(\"a=>{0}\".format(a))\n",
    "b -= 5\n",
    "print(\"b=>{0}\".format(b))\n",
    " \n",
    " \n",
    "print('\\n次方：')\n",
    "# d是b的2次方\n",
    "# d is squared of b.\n",
    "d = b**2\n",
    "print(\"d=>{0}\".format(d))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "structural-wesley",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a=>[0 1 2 3 4]\n",
      "b=>[10  9  8  7  6]\n",
      "\n",
      "同除2:\n",
      "c=>[0.  0.5 1.  1.5 2. ]\n",
      "\n",
      "同乘2:\n",
      "d=>[20 18 16 14 12]\n"
     ]
    }
   ],
   "source": [
    "a = np.arange(5)\n",
    "b = np.arange(10, 5, -1)\n",
    "print(\"a=>{0}\".format(a))\n",
    "print(\"b=>{0}\".format(b))\n",
    "print(\"\\n同除2:\")\n",
    "# c等於a同除以2\n",
    "c = a / 2\n",
    "print(\"c=>{0}\".format(c))\n",
    " \n",
    "print(\"\\n同乘2:\")\n",
    "# d等於b同乘以2\n",
    "d = b * 2\n",
    "print(\"d=>{0}\".format(d))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "sunrise-azerbaijan",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2]\n",
      " [3 4]]\n",
      "[[5 6]\n",
      " [7 8]]\n",
      "A, B相乘(矩陣乘法) =>\n",
      "[[19 22]\n",
      " [43 50]]\n",
      "\n",
      "A, B相對應位置相乘=>\n",
      "[[ 5 12]\n",
      " [21 32]]\n"
     ]
    }
   ],
   "source": [
    "# 矩陣相乘\n",
    "A = np.array([[1, 2], [3, 4]])\n",
    "B = np.array([[5, 6], [7, 8]])\n",
    "print(A)\n",
    "print(B)\n",
    "print(\"A, B相乘(矩陣乘法) =>\\n{0}\".format(A.dot(B)))\n",
    "print()\n",
    "print(\"A, B相對應位置相乘=>\\n{0}\".format(A*B))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "skilled-jacksonville",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
