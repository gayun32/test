"""
나만의 프롬프트 관리 프로그램
"""

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def get_default_prompts():
    """이전 미션에서 작성한 프롬프트를 기본 데이터로 등록한다."""
    return [
        {
            "title": "블로그 글 작성 도우미",
            "content": (
                "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 "
                "SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 "
                "구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요."
            ),
            "category": "텍스트 생성",
            "favorite": True,
        },
        {
            "title": "제품 썸네일 생성",
            "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 배경은 깔끔한 단색으로 하고 제품이 돋보이도록 구성해주세요.",
            "category": "이미지 생성",
            "favorite": False,
        },
        {
            "title": "IT 컨설턴트 페르소나",
            "content": "당신은 15년 경력의 IT 컨설턴트입니다. 기업의 디지털 전환 전략을 조언하는 역할을 수행해주세요.",
            "category": "페르소나",
            "favorite": False,
        },
    ]


def get_nonempty_input(label):
    """빈 값이 입력되면 다시 입력을 요청한다."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("  ↳ 입력값이 비어있어요. 다시 입력해주세요.\n")


def choose_category():
    """카테고리를 목록에서 선택하거나 직접 입력한다."""
    print("\n▷ 카테고리를 골라주세요")
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"   ({i}) {category}")
    print("   (0) 직접 입력할래요")

    choice = input(">> ").strip()

    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(CATEGORIES):
            return CATEGORIES[idx - 1]
        elif idx == 0:
            return get_nonempty_input("카테고리 이름 입력 >> ")

    if choice:
        return choice
    return get_nonempty_input("카테고리 이름 입력 >> ")


def add_prompt(prompts):
    """새로운 프롬프트를 등록한다."""
    print("\n✏️  새 프롬프트 등록")
    print("-" * 30)
    title = get_nonempty_input("제목 >> ")
    content = get_nonempty_input("내용 >> ")
    category = choose_category()

    prompts.append(
        {
            "title": title,
            "content": content,
            "category": category,
            "favorite": False,
        }
    )
    print("\n✅ 등록 완료! 새 프롬프트가 보관함에 저장되었어요.")

def format_prompt_line(index, prompt):
    """목록 출력용 한 줄 포맷을 만든다."""
    star = " ⭐" if prompt["favorite"] else ""
    return f"  {index:>2}. [{prompt['category']}] {prompt['title']}{star}"


def show_list(prompts):
    """저장된 모든 프롬프트를 번호와 함께 출력한다."""
    print("\n📋 전체 프롬프트 목록")
    print("-" * 30)
    if not prompts:
        print("  아직 등록된 프롬프트가 없어요.")
        return

    for i, prompt in enumerate(prompts, start=1):
        print(format_prompt_line(i, prompt))
    print("-" * 30)
    print(f"  총 {len(prompts)}개의 프롬프트가 있어요.")

def show_menu():
    """메인 메뉴를 출력하고 사용자의 선택을 반환한다."""
    print("\n💙🐬 나만의 프롬프트 보관함 🐬💙")
    print("=" * 32)
    print("[1] 새 프롬프트 등록하기")
    print("[2] 전체 프롬프트 둘러보기")
    print("[3] 카테고리로 찾아보기")
    print("[4] 키워드로 검색하기")
    print("[5] 프롬프트 자세히 보기")
    print("[6] 즐겨찾기 켜고 끄기")
    print("[7] 즐겨찾기 모아보기")
    print("[0] 프로그램 나가기")
    print("=" * 32)

    return input("원하는 번호를 입력하세요 >> ").strip()


def main():
    prompts = get_default_prompts()

    print("\n환영합니다! 프롬프트 보관함을 시작할게요 :)")

    while True:
        choice = show_menu()

        if choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            show_list(prompts)
        elif choice == "0":
            print("\n👋 프로그램을 종료합니다. 다음에 또 만나요!")
            break
        else:
            print("\n  ↳ 아직 준비 중인 기능이에요.")


if __name__ == "__main__":
    main()