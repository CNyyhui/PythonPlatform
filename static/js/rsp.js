// 为所有选择按钮添加点击事件监听器
document.querySelectorAll('.choice-button').forEach(button => {
    button.addEventListener('click', function() {
        // 获取用户选择的选项
        const userChoice = this.getAttribute('data-choice');

        // 向服务器发送用户的选择
        fetch('/rsp/play_rsp', {
            method: 'POST', // 使用 POST 方法
            headers: {
                'Content-Type': 'application/json' // 设置请求头为 JSON 格式
            },
            body: JSON.stringify({ choice: userChoice }) // 将用户选择转为 JSON 字符串
        })
        .then(response => response.json()) // 解析服务器返回的 JSON 响应
        .then(data => {
            // 更新结果显示
            document.getElementById('result').innerText = `你选择了 ${userChoice}，电脑选择了 ${data.computer_choice}. ${data.result}`;
            document.getElementById('user-score').innerText = `你: ${data.user_score}`; // 更新用户分数
            document.getElementById('computer-score').innerText = `电脑: ${data.computer_score}`; // 更新电脑分数

            // 更新获胜者信息
            const overallWinnerElement = document.getElementById('overall-winner');
            if (data.overall_winner) { // 如果有获胜者
                overallWinnerElement.innerText = data.overall_winner; // 显示获胜者
                // 根据获胜者改变文本颜色
                if (data.overall_winner.includes('你')) {
                    overallWinnerElement.style.color = 'red'; // 用户获胜时显示红色
                } else {
                    overallWinnerElement.style.color = 'blue'; // 电脑获胜时显示蓝色
                }
            } else {
                overallWinnerElement.innerText = ''; // 清空获胜者信息
                overallWinnerElement.style.color = ''; // 恢复默认颜色
            }
        });
    });
});

// 为重置按钮添加点击事件监听器
document.getElementById('reset-button').addEventListener('click', function() {
    // 发送重置请求到服务器
    fetch('/rsp/reset_rsp', {
        method: 'POST' // 使用 POST 方法
    })
    .then(response => response.json()) // 解析服务器返回的 JSON 响应
    .then(data => {
        // 清空结果和分数显示
        document.getElementById('result').innerText = '';
        document.getElementById('user-score').innerText = '你: 0'; // 重置用户分数
        document.getElementById('computer-score').innerText = '电脑: 0'; // 重置电脑分数
        document.getElementById('overall-winner').innerText = ''; // 清空获胜者信息
    });
});