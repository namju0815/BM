//addEventListener("이벤트 type", 실행할 함수)
document.addEventListener("DOMContentLoaded", function() {
    //배너-변수
    const bannerContainer = document.querySelector(".banner-container") //배너틀
    const slides = document.querySelectorAll(".banner-slide") //각각의 배너들
    let currentIndex = 0 //현재 배너 index
    let maxSlide = slides.length; //전체 배너길이

    //배너-슬라이드 함수
    function slideShow(index){
        slides.forEach((slide, i) => {
            slide.classList.remove("pre", "active", "next");
        });
        //새로운 클래스를 생성해서 이전 배너, 현재 배너, 다음 배너를 지정하고 transform으로 이동시킴!!!!
        slides[index].classList.add("active");
        if (index == 0){ //첫번쨰 배너
            slides[maxSlide-1].classList.add("pre"); //맨뒤
            slides[1].classList.add("next"); //두번째
        } else if(index < maxSlide - 1){
            slides[index + 1].classList.add("next");
            slides[index - 1].classList.add("pre");
        } else{ //마지막 배너
            slides[index - 1].classList.add("pre"); //이전배너
            slides[0].classList.add("next");
        }
    }

    //배너-자동 재생
    function autoPlay(){
        currentIndex = (currentIndex+1) % maxSlide;
        slideShow(currentIndex);
    }
    slideShow(currentIndex);
    let valid = setInterval(autoPlay, 3000);

    //배너-마우스가 위에 올라갔을 떄 정지
    bannerContainer.addEventListener("mouseenter", function(){
        clearInterval(valid);
    });

    //배너-마우스가 내려가면 다시 재생
    bannerContainer.addEventListener("mouseleave", function(){
        valid = setInterval(autoPlay, 3000);
    });

});

document.addEventListener("DOMContentLoaded", function () {
    const menulistItems = document.querySelectorAll(".menulist-a"); //링크들

    menulistItems.forEach(function (menulistItem) {
        menulistItem.addEventListener("click", function (event) {
            event.preventDefault(); //페이지 넘어가는 것을 막음

            if (!isLoggedIn) {
                alert("로그인이 필요합니다. 로그인 페이지로 이동합니다.");
                // 로그인 페이지로 이동하거나 다른 처리를 추가할 수 있습니다.
                window.location.href = "/login";
            } else {
                window.location.href = menulistItem.getAttribute("href");
            }
        });
    });
});