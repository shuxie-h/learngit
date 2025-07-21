if __name__ == "__main__":
    start = "2025-04-01"
    print(start)
    end = "2025-05-01"
    print(end)
    action_cz = OnlineReport(
        start_date=start,
        end_date=end,
        jira_assignee="储值",
        period="month",
        dimension="jira_module",
        data_type="1",
        add_document=False,
        send_message=True,
        receive_message_name="huxiaojun_hu",
        receive_message_type="private_chat",
        receive_message_addr="https://open.feishu.cn/open-apis/bot/v2/hook/c1d9bde3-b3ba-45a4-bb07-8f658299fdd3",
    )
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(action_cz.report_data_main())



print("hello world")
print("hello world")

    