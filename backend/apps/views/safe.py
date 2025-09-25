import json
from typing import List, Dict
from .llm import lm as foundation_model  # 引入全局对象 foundation_model
import re

# 假设评论数据文件的路径
COMMENTS_FILE = 'D:\\Documents\\SE-Smart-Comment-Sys-main\\backend\\lib\\data\\Gen\\extreme_comments.json'
REMOVED_COMMENTS_FILE = 'D:\\Documents\\SE-Smart-Comment-Sys-main\\backend\\lib\\data\\Gen\\removed_comments.json'

# 内容政策示例
CONTENT_POLICY = {
    "C0": "Non-inappropriate content",
    "C1": "Other inappropriate content",
    "C2": "Inappropriate content (discriminatory remarks, obscene content, etc.)",
    "C3": "Harassment or bullying",
    "C4": "Hate speech or threats"
}

# 定义不良内容关键词列表（用于辅助判断）
INAPPROPRIATE_KEYWORDS = [
    "discriminatory", "obscene", "bullying", "threat",
    "hate", "offensive", "abusive", "violent", "racist",
    "bias", "harassment", "kill", "attack", "destroy",
    "stupid", "dumb", "worthless", "ugly", "retarded"
]

# 设置正则表达式模式匹配关键词（忽略大小写）
KEYWORD_PATTERN = re.compile("|".join(INAPPROPRIATE_KEYWORDS), re.IGNORECASE)

def load_comments(file_path: str) -> List[Dict]:
    """加载评论数据"""
    with open(file_path, 'r') as file:
        courses = json.load(file)
    return courses

def classify_content_with_llm(content: str) -> str:
    """
    使用 LLM 模型生成一个输出来判断内容的分类。
    基于模型生成的响应进行不良内容分类。
    """
    system_msg = (
        "Please classify the following comment based on the content policy into one of the categories: "
        "C0 (Non-inappropriate content), "
        "C1 (Other inappropriate content), "
        "C2 (Inappropriate content, such as discriminatory remarks, obscene content, etc.), "
        "C3 (Harassment or bullying), "
        "or C4 (Hate speech or threats). "
        "Make sure to carefully consider the context and the implications of the comment. "
        "Respond with the category code (C0, C1, C2, C3, or C4) only."
    )
    user_msg = f"Comment: {content}"

    # 使用 LLM 模型生成分析文本
    response = foundation_model.forward_text(system_msg=system_msg, user_msg=user_msg)
    print(f"Response: {response}")
    # 假设 response 是一个直接的分类结果字符串
    analysis = response.strip()

    # 提取分析结果中的分类
    for label in CONTENT_POLICY.keys():
        if label in analysis:
            return label

    # 如果未能找到匹配的标签，返回默认的其他不良内容
    return "C1"

def is_inappropriate(content: str) -> bool:
    """
    使用LLM生成的响应和简单的关键词匹配来判断内容是否不适当。
    """
    classification = classify_content_with_llm(content)

    # 检查是否分类为 C0 之外的任何内容
    if classification != "C0":
        print(f"Inappropriate content detected by LLM: {classification}")
        return True

    # 使用关键词和正则表达式进行额外的检查
    if KEYWORD_PATTERN.search(content):
        print(f"Inappropriate keyword detected in content: {content}")
        return True

    return False

def moderate_comments(courses: List[Dict]):
    """过滤掉不良评论并保留被删除的评论记录"""
    filtered_courses = []
    removed_comments = []

    for course in courses:
        filtered_comments = {'extreme' : []}

        for comment in course['comments']:
            for comment_type, content in comment.items():
                if not is_inappropriate(content):
                    filtered_comments[comment_type].append(content)
                else:
                    print(f"Removed inappropriate {comment_type} comment: {content}")
                    removed_comments.append({
                        'course': course['name'],
                        'type': comment_type,
                        'content': content
                    })

        filtered_courses.append({
            'name': course['name'],
            'comments': filtered_comments
        })

    return filtered_courses, removed_comments


def save_comments(courses: List[Dict], file_path: str) -> None:
    """保存过滤后的评论数据"""
    with open(file_path, 'w') as file:
        json.dump(courses, file, indent=4)


def save_removed_comments(removed_comments: List[Dict], file_path: str) -> None:
    """保存被删除的评论记录"""
    with open(file_path, 'w') as file:
        json.dump(removed_comments, file, indent=4)


def main():
    """主流程"""
    # 加载评论数据
    courses = load_comments(COMMENTS_FILE)

    # 审核评论
    filtered_courses, removed_comments = moderate_comments(courses)

    # 保存过滤后的评论
    save_comments(filtered_courses, COMMENTS_FILE)

    # 保存被删除的评论记录
    save_removed_comments(removed_comments, REMOVED_COMMENTS_FILE)


if __name__ == '__main__':
    main()
