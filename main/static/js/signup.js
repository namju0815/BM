function id_overlap_check() {
    const usernameInput = document.getElementById("username");
    const username = usernameInput.value;

    // 중복 체크를 수행하기 전에 사용자가 유효한 ID를 입력했는지 확인
    if (!username) {
        alert("유효한 사용자 이름을 입력하세요.");
        return;
    }

    // 서버로 중복 체크 요청을 보냄
    fetch(`/check_username/?username=${username}`)
        .then(response => response.json())
        .then(data => {
            if (data.is_taken) {
                alert("이미 사용 중인 사용자 이름입니다. 다른 이름을 입력하세요.");
            } else {
                document.querySelector('.id-check-success').style.display = 'block';
                document.querySelector('.id-overlap-btn').style.display = 'none';
                alert("사용 가능한 사용자 이름입니다!");
            }
        })
        .catch(error => {
            console.error("Error during username check:", error);
            alert("중복 체크 중 오류가 발생했습니다. 다시 시도해주세요.");
        });
}