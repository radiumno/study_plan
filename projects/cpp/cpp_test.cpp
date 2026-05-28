/**
 * C++ 水平摸底测试
 *
 * 从第1题开始往下做,做到哪题卡住了就停.
 * 不用全部做完,做到不会的题就告诉我你做到第几题.
 * 每题写完整可运行的代码.
 */

// ============================================================
// 第1题(基础)
// 写一个程序,输入两个整数,输出它们的和,差,积,商.
// ============================================================
#include <iostream>
using namespace std;
class Function
{
public:
  virtual int func(int a, int b) = 0;
  virtual ~Function() = default;
};

class Add : public Function
{
public:
  int func(int a, int b) override
  {
    return a + b;
  }
};

class Sub : public Function
{
public:
  int func(int a, int b) override
  {
    return a - b;
  }
};

class Mul : public Function
{
public:
  int func(int a, int b) override
  {
    return a * b;
  }
};

class Div : public Function
{
public:
  int func(int a, int b) override
  {
    if (b == 0)
    {
      cout << "Error: Division by zero!" << endl;
      return 0;
    }
    return a / b;
  }
};

int myCalculator(int a, int b, Function *op)
{
  return op->func(a, b);
}

void testProblem1()
{
  cout << "===== 第1题 =====" << endl;
  cout << "10 + 5 = " << myCalculator(10, 5, new Add()) << endl;
  cout << "10 - 5 = " << myCalculator(10, 5, new Sub()) << endl;
  cout << "10 * 5 = " << myCalculator(10, 5, new Mul()) << endl;
  cout << "10 / 5 = " << myCalculator(10, 5, new Div()) << endl;
}

// ============================================================
// 第2题(控制流)
// 写一个函数 isPrime(int n) 判断素数,然后在 main 里打印 1-100 的所有素数.
// ============================================================
bool isPrime(int n)
{
  if (n <= 1)
    return false;
  for (int i = 2; i * i <= n; i++)
  {
    if (n % i == 0)
      return false;
  }
  return true;
}

void testProblem2()
{
  cout << "\n===== 第2题 =====" << endl;
  for (int i = 1; i <= 100; i++)
  {
    if (isPrime(i))
      cout << i << " ";
  }
  cout << endl;
}

// ============================================================
// 第3题(数组/容器)
// 写一个函数,接受一个 vector<int>,返回去重后的 vector(顺序不变).
// 例:输入 [1, 2, 2, 3, 1, 4] → 返回 [1, 2, 3, 4]
// ============================================================
#include <vector>
std::vector<int> removeDuplicates(std::vector<int> &vec)
{
  std::vector<int> new_vector;
  for (int i = 0; i < vec.size(); i++)
  {
    if (!isFind(new_vector, vec[i]))
    {
      new_vector.push_back(vec[i]);
    }
  }
  return new_vector;
}
bool isFind(std::vector<int> &vec, int num)
{
  for (int i = 0; i < vec.size(); i++)
  {
    if (vec[i] == num)
    {
      return true;
    }
  }
  return false;
}

// ============================================================
// 第4题(类与面向对象)
// 设计一个 BankAccount 类:
//   - 私有成员:账户名(string),余额(double)
//   - 公有方法:存款,取款,查询余额
//   - 取款不能透支(余额不足时打印错误并拒绝)
// 在 main 中演示使用.
// ============================================================
class BankAccount
{
private:
  string accountName;
  double balance;

public:
  void saveMoney(double money)
  {
    balance += money;
  }
  bool isEnoughMoney(double money)
  {
    if (balance >= money)
    {
      return true;
    }
    else
    {
      cout << "Error: Insufficient funds!" << endl;
      return false;
    }
  }
  void takeMoney(double money)
  {
    if (isEnoughMoney(money))
    {
      balance -= money;
    }
  }
  double getBalance()
  {
    return balance;
  }
};
// ============================================================
// 第5题(继承与多态)
// 设计一个 Shape 基类和 Circle/Rectangle 派生类:
//   - Shape 有纯虚函数 area() 和 name()
//   - Circle 由半径构造,Rectangle 由宽高构造
//   - 在 main 中用 vector<Shape*> 存储多种形状并打印面积
// ============================================================
class Shape
{
public:
  virtual double area() = 0;
  virtual string name() = 0;
};
class Circle : public Shape
{
private:
  double radius;

public:
  Circle(double r) : radius(r) {}
  double area() override
  {
    return 3.14159 * radius * radius;
  }
  string name() override
  {
    return "Circle";
  }
};
class Rectangle : public Shape
{
private:
  double width;
  double height;

public:
  Rectangle(double w, double h) : width(w), height(h) {}
  double area() override
  {
    return width * height;
  }
  string name() override
  {
    return "Rectangle";
  }
};
void testProblem5()
{
  vector<Shape *> shapes;
  shapes.push_back(new Circle(5));
  shapes.push_back(new Rectangle(4, 6));
  for (Shape *shape : shapes)
  {
    cout << shape->name() << " area: " << shape->area() << endl;
  }
}
// ============================================================
// 第6题(模板/STL进阶)
// 写一个模板函数,接受任意类型的 vector,返回排序后的新 vector(不修改原数据).
// 再写一个特化版本,当元素类型为 const char* 时按字符串长度排序.
// ============================================================
template <typename T>

vector<T> sortVector(const vector<T> &vec)
{
  vector<T> new_vector = vec;
  for (int i = 0; i < vec.size(); i++)
  {
    T min = vec[i];
    for (int j = i + 1; j < vec.size(); j++)
    {
      if (vec[j] < min)
      {
        min = vec[j];
      }
    }
    new_vector[i] = min;
  }
  return new_vector;
}

// ============================================================
// 第7题(内存管理)
// 实现一个简单的 unique_ptr 替代品:
//   - 模板类 MyUniquePtr<T>
//   - 构造函数接受 T*
//   - 禁止拷贝,支持移动语义
//   - 提供 operator* 和 operator->
//   - 析构时自动 delete
// ============================================================
