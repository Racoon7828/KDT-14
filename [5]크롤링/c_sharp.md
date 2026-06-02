작성해주신 강의 메모와 코드를 바탕으로 객체지향 프로그래밍(OOP)의 핵심 개념과 C#, Python 각 언어의 특징을 정리한 내용입니다.

---

## 1. 클래스와 객체지향 프로그래밍(OOP)의 핵심

클래스를 도입하고 사용하는 궁극적인 목적은 **코드의 재사용성**과 **유지보수성의 향상**입니다.

* **데이터와 함수의 결합:** 과거에는 함수와 데이터가 완전히 독립적이라고 여겨졌으나, 이 둘을 하나의 객체(Object)로 묶어서 관리하는 것이 논리적이고 효율적이라는 배경에서 발전했습니다.
* **그룹화:** 같은 기능을 수행하는 속성들을 모아 중복 코드를 방지합니다.
* **상속과 다형성:** 파이썬은 언어 자체적으로 다형성을 유연하게 지원하며, C#, C++, Java 같은 언어는 클래스를 기반으로 다형성을 구현합니다.
* **캡슐화 (Encapsulation):** 객체의 내부(멤버 변수)는 철저히 감추고, 외부로 드러나는 것(함수/인터페이스)만 제공합니다. 이를 통해 클래스를 사용하는 사람이 내부 동작 방식을 몰라도 쉽게 사용할 수 있도록 돕습니다.

---

## 2. C# 관점: 캡슐화와 프로퍼티 (Property)

C#에서는 접근 제한자(`private`, `public`)와 접근자(Getter/Setter)를 통해 캡슐화를 엄격하게 구현합니다.

### C# 클래스 구조의 주요 특징

* **private 변수:** 외부 접근을 차단하여 프로그래머의 실수를 막습니다. 클래스를 '만드는 입장'과 '사용하는 입장'을 분리하여 데이터를 보호합니다.
* **Getter / Setter 메서드:** 사용자는 내부 구조나 데이터 검증 로직을 몰라도 제공된 메서드만 호출하여 안전하게 값을 변경할 수 있습니다.
* **프로퍼티 (Property):** 겉보기에는 일반 변수에 값을 대입(`a.Name2 = "김지우"`)하는 것 같지만, 실제로는 내부적으로 함수(`set`, `get`)가 호출되는 구조를 가집니다.

```csharp
using System;

class Pokemon
{
    // 1. private 변수 (캡슐화: 외부 접근 불가)
    private string name;
    private string name2;

    // 2. 접근자 (Getter / Setter)
    public void SetName(string name)
    {
        // 이름 길이 확인, 특수문자 확인, DB 저장 등의 내부 로직 수행
        this.name = name;
    }

    public string GetName()
    {
        return name;
    }

    // 3. 프로퍼티 (Property) - 함수 호출을 변수처럼 사용
    public string Name2
    {
        get
        {
            return name2;
        }
        set
        {
            name2 = value;
        }
    }

    // 4. 자동 구현 프로퍼티 (Auto-implemented Property)
    public string Name { get; set; }
    public int Level { get; set; }

    // 생성자
    public Pokemon(string name, int level)
    {
        Name = name;
        Level = level;
    }

    public void Attack()
    {
        Console.WriteLine($"{Name} attacks with power {Level * 10}!");
    }
}

class Program
{
    static void Main()
    {
        var p = new Pokemon("김기석", 1);
        p.SetName("김지우"); // 내부 구현을 몰라도 설정 가능
        p.Attack();
    }
}

```

---

## 3. Python 관점: 객체와 동적 할당

파이썬에서 클래스는 "딕셔너리(Dictionary)에 함수를 섞어놓은 형태"와 유사하게 동작합니다. 변수(데이터)를 바닥에 흩뿌려 선언하지 않고, 특정 객체 내부에 집어넣어 그룹화하는 것이 핵심입니다.

### 파이썬 클래스 구조의 주요 특징

* **self 매개변수:** 메서드가 호출될 때, 호출한 주체(객체 자신)를 가리킵니다.
* **동적 멤버 할당:** C#과 달리 변수를 미리 선언하지 않아도, 인스턴스화된 객체에 외부에서 직접 멤버 변수(Attribute)를 추가하고 할당할 수 있습니다.

```python
class Pokemon:
    def attack(self):
        # self: 이 메서드를 호출한 주체(객체)
        print(f"{self.name}이(가) 공격한다! (레벨: {self.level})")

# 객체(Object) 생성: 그룹화된 변수와 함수의 집합체
pikachu = Pokemon()

# 멤버 변수 동적 할당 (Attribute)
# 변수를 따로 선언하지 않고 pikachu 객체 내부에 보관
pikachu.name = "Pikachu" 
pikachu.level = 5

# 멤버 변수 접근 및 함수 호출
print(pikachu.name)
print(pikachu.level)
pikachu.attack()

```