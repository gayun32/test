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
    print("\n환영합니다! 프롬프트 보관함을 시작할게요 :)")

    while True:
        choice = show_menu()

        if choice == "0":
            print("\n👋 프로그램을 종료합니다. 다음에 또 만나요~!")
            break
        else:
            print("\n  ↳ 아직 준비 중인 기능이에요.")


if __name__ == "__main__":
    main()