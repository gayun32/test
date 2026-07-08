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
    prompts = get_default_prompts()  # ← 기본 데이터 불러오기

    print("\n환영합니다! 프롬프트 보관함을 시작할게요 :)")

    while True:
        choice = show_menu()

        if choice == "0":
            print("\n👋 프로그램을 종료합니다. 다음에 또 만나요!")
            break
        else:
            print("\n  ↳ 아직 준비 중인 기능이에요.")


if __name__ == "__main__":
    main()