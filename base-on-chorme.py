import random
import threading
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def auto_fillout(url):

    # 可以避免智能验证码的选项
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)

    # 创建 Chrome 浏览器对象
    browser = webdriver.Chrome(options=option)
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    browser.get(url)
    time.sleep(2)

    rooms = browser.find_elements(By.CSS_SELECTOR, '.el-input__icon.el-icon-arrow-down')
    for index, room in enumerate(rooms):
        room.click()
        if index == 0:
            try:
                element1 = browser.find_elements(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/ul/li/span")
                # 检查第一列是否有选项
                if element1:
                    # 固定选择一个选项
                    option1 = element1[1]

                    # 点击选择的选项
                    browser.execute_script("arguments[0].click();", option1)
                time.sleep(2)

                # 第二列
                element2 = browser.find_elements(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/ul/li/span")
                # 检查第二列是否有选项
                if element2:
                    # 随机选择一个选项
                    option2 = random.choice(element2)

                    # 点击随机选择的选项
                    browser.execute_script("arguments[0].click();", option2)
                time.sleep(2)

            except Exception as e:
                print(f"Error selecting cascader options: {e}")
            time.sleep(5)

        elif index == 1:
            # 所在地

            try:
                # 第一列
                sheng = browser.find_elements(By.XPATH, "/html/body/div[3]/div[1]/div/div[1]/ul/li/span")
                # 检查第一列是否有选项
                if sheng:
                    # 随机选择一个选项
                    option1 = random.choice(sheng)

                    # 点击选择的选项
                    browser.execute_script("arguments[0].click();", option1)
                time.sleep(2)

                # 第二列
                shi = browser.find_elements(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/ul/li/span")
                # 检查第二列是否有选项
                if shi:
                    # 随机选择一个选项
                    option2 = random.choice(shi)

                    # 点击随机选择的选项
                    browser.execute_script("arguments[0].click();", option2)

                # 第三列
                qv = browser.find_elements(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div[1]/ul/li/span")

                if qv:
                    # 随机选择一个选项
                    option3 = random.choice(qv)

                    # 点击随机选择的选项
                    browser.execute_script("arguments[0].click();", option3)
                time.sleep(2)

            except Exception as e:
                print(f"Error selecting cascader options: {e}")

        elif index == 2:
            # 网龄

            try:
                # 第一列
                column1 = browser.find_elements(By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[1]/ul/li/span")
                # 检查第一列是否有选项
                if column1:
                    # 选择一个选项
                    option1 = column1[1]

                    # 点击随机选择的选项
                    browser.execute_script("arguments[0].click();", option1)
                time.sleep(2)

                # 第二列
                column2 = browser.find_elements(By.XPATH, "/html/body/div[4]/div[1]/div[2]/div[1]/ul/li/span")
                # 检查第二列是否有选项
                if column2:
                    # 随机选择一个选项
                    random_index = random.randint(0, 5)
                    option2 = column2[random_index]
                    # option2 = random.choice(column2)

                    # 点击随机选择的选项
                    browser.execute_script("arguments[0].click();", option2)
                time.sleep(2)

            except Exception as e:
                print(f"Error selecting cascader options: {e}")

    # 单选题
    answerxx = browser.find_elements(By.CSS_SELECTOR, '.el-radio')
    num = len(answerxx)
    a1 = random.randint(0, 1)
    a2 = random.randint(5, 7)
    a3 = 14
    a4 = 23
    a5 = random.randint(24, 25)
    a6 = random.randint(26, 29)
    a7 = random.randint(32, 36)
    a8 = random.randint(37, 41)
    a9 = random.randint(44, 46)
    a10 = random.randint(47, 48)
    a11 = random.randint(52, 53)
    for index, answer in enumerate(answerxx):
        if index == a1 or index == a2 or index == a3 or index == a4 or index == a5 or index == a6 or index == a7 or index == a8 or index == a9 or index == a10 or index == a11:
            try:
                answer.click()
                time.sleep(1)
            except Exception as e:
                print("error clickx!!!")

    # 评分
    random_numbers = [random.randint(7, 9) for _ in range(12)]
    # 找出7、8、9各自所在的位置
    positions_7 = [index for index, num in enumerate(random_numbers) if num == 7]
    positions_8 = [index for index, num in enumerate(random_numbers) if num == 8]
    positions_9 = [index for index, num in enumerate(random_numbers) if num == 9]

    answer7 = browser.find_elements(By.CSS_SELECTOR, '.el-rate .el-rate__item:nth-child(7)')
    for index, answer in enumerate(answer7):
        if index in positions_7:
            try:
                answer.click()
                time.sleep(1)
            except Exception as e:
                print("error clickx!!!")

    answer8 = browser.find_elements(By.CSS_SELECTOR, '.el-rate .el-rate__item:nth-child(8)')
    for index, answer in enumerate(answer8):
        if index in positions_8:
            try:
                answer.click()
                time.sleep(1)
            except Exception as e:
                print("error clickx!!!")

    answer9 = browser.find_elements(By.CSS_SELECTOR, '.el-rate .el-rate__item:nth-child(9)')
    for index, answer in enumerate(answer9):
        if index in positions_9:
            try:
                answer.click()
                time.sleep(1)
            except Exception as e:
                print("error clickx!!!")

    # 多选题

    # 定位所有多选题组
    groups = browser.find_elements(By.CSS_SELECTOR, '.tc-checkbox-group')

    for group in groups:
        # 定位每组内的复选框
        checkboxes = group.find_elements(By.CSS_SELECTOR, '.el-checkbox__input')
        # 随机选择几个复选框进行点击
        selected_checkboxes = random.sample(checkboxes[:-1], k=random.randint(1, len(checkboxes) - 2))

        for checkbox in selected_checkboxes:
            try:
                # 确保元素可交互
                if not checkbox.is_displayed():
                    element_position = group.location_once_scrolled_into_view
                    browser.execute_script("window.scrollTo(%s, %s);" % (element_position['x'], element_position['y']))
                checkbox.click()
                time.sleep(1)
            except Exception as e:
                print(f"Error clicking checkbox in group: {e}")

    time.sleep(10)
    # 提交
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.el-button.el-button--primary.el-button--large")
    submit_button.click()

    time.sleep(random.randint(4, 8))

    browser.quit()


# 脚本主入口
if __name__ == "__main__":
    # 用户输入要运行的次数
    num_runs = int(input("请输入要运行的次数: "))
    num_xian = int(input("线程数：(推荐2-5)"))
    num = str(input("请输入你二维码对应的六位数字："))

    url0 = "https://myd.iscn.org.cn/#/s/6rPmYeqD?sourceId="  # 这是问卷的 URL
    url = url0 + num
    print("可以检查一下链接是否正确", end="")
    print(url)

    # 创建并启动线程的循环
    for i in range(num_runs):
        # 创建线程列表以跟踪所有线程
        threads = []
        for j in range(num_xian):  # 这里假设你总是想要启动3个线程
            thread = threading.Thread(target=auto_fillout, args=(url,))
            threads.append(thread)
            thread.start()
            print(f"启动线程 {thread.name} 进行第 {i+1} 次运行")

            # 这里可以添加 sleep 来控制启动线程的间隔，如果需要的话
            time.sleep(random.randint(1,3))

        # 等待所有线程完成
        for thread in threads:
            thread.join()
            print(f"线程 {thread.name} 完成")

        print(f"第 {i+1} 次运行完成")
