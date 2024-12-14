from setuptools import setup, find_packages

setup(
    name="handgpt",                     # 包名，用户通过 pip install <name> 安装
    version="0.1.1",                    # 版本号
    author="Xener",                     # 作者
    author_email="github@handgpt.app",  # 作者邮箱
    description="A simple tool for HandGPT",  # 简短描述
    long_description=open("README.md").read(),  # 详细描述（来自 README.md）
    long_description_content_type="text/markdown",  # README 文件格式
    url="https://github.com/handgpt/HandGPT",  # 项目主页（GitHub 链接等）
    packages=find_packages(where="core/src"),      # 查找 src 目录中的包
    package_dir={"": "core/src"},                  # 指定包的根目录为 src
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",            # 需要的 Python 版本
    install_requires=[
        "websockets>=14.1",             # 依赖包及版本要求
    ],
    license="MIT",
)
