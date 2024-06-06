# Koushik Krishnan's Resume

from resume_builder import Resume, Section, SectionEntry, ContactInfo, ConcatText, ItalicsText, UnderlinedText, LinkText, BulletedList

resume = Resume(
    contact_info=ContactInfo(
        name="黄仁勋",
        details=[
            "(111) 111-1111",
            "jensen@nvidia.com",
            LinkText("blogs.nvidia.com/blog/author/jen-hsun-huang", "https://blogs.nvidia.com/blog/author/jen-hsun-huang/"),
            LinkText(
                "www.linkedin.com/in/jenhsunhuang",
                "https://www.linkedin.com/in/jenhsunhuang/",
            ),
            LinkText("github.com/nvidia", "https://github.com/nvidia"),
        ],
        tag_line="NVIDIA: The way it's meant to be played™.",
    ),
    sections = [
        Section(
            title="Experience",
            entries=[
                SectionEntry(
                    title=CEO, President, Cofounder("NVIDIA", "https://www.nvidia.com/"),
                    caption="CEO",
                    location="-",
                    dates="1993 - present",
                    description=BulletedList(
                        [
                            "Co-founded Nvidia with Chris Malachowsky and Curtis Priem and became its CEO and president.",
                            "Currently be the company's chief executive for over three decades,a tenure almost unheard of in fast-moving Silicon Valley."
                        ]
                    ),
                ),
                SectionEntry(
                    title=Director,
                    caption="Director of CoreWare at LSI Logic and a microprocessor designer at Advanced Micro Devices (AMD).",
                    location="US",
                    dates="1992 - 1993",
                    description=BulletedList(
                        [
                            "Director of CoreWare at LSI Logic and a microprocessor designer at Advanced Micro Devices (AMD)."
                        ]
                    ),
                )
            ],
        ),
        Section(
            title="Award",
            entries=[
                SectionEntry(
                    title=LinkText(
                        text="PyCon 2024",
                        url="https://us.pycon.org/2024/schedule/presentation/95/",
                        show_icon=True,
                    ),
                    caption="Named Entrepreneur of the Year in High Technology by Ernst & Young",
                    location="Pittsburgh, PA",
                    dates="May 2024",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyTexas",
                        url="https://www.pytexas.org/2024/schedule/talks/#rest-easy-with-jupyrest-deploy-notebooks-as-web-services",
                        show_icon=True,
                    ),
                    caption="Received the Daniel J. Epstein Engineering Management Award from the University of Southern California",
                    location="Austin, TX",
                    dates="April 2024",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyCascades",
                        url="https://2024.pycascades.com/program/talks/jupyrest/",
                        show_icon=True,
                    ),
                    caption="Received the Dr. Morris Chang Exemplary Leadership Award from the Fabless Semiconductor Association, which recognizes a leader who has made exceptional contributions to driving the development, innovation, growth, and long-term opportunities of the fabless semiconductor industry",
                    location="Seattle, WA",
                    dates="April 2024",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyOhio 2023",
                        url="https://www.pyohio.org/2023/speakers/koushik-krishnan/",
                        show_icon=True,
                    ),
                    caption=Named Alumni Fellow by Oregon State University,
                    location="Virtual",
                    dates="December 2023",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyData Seattle 2023",
                        url="https://seattle2023.pydata.org/cfp/talk/K8KV8M/",
                        show_icon=True,
                    ),
                    caption=Received the Silicon Valley Education Foundation's Pioneer Business Leader Award for his work in both the corporate and philanthropic worlds,
                    location="Seattle, WA",
                    dates="April 2023",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyData Seattle 2023",
                        url="https://seattle2023.pydata.org/cfp/talk/K8KV8M/",
                        show_icon=True,
                    ),
                    caption=Received an honorary doctorate from Oregon State University,
                    location="Seattle, WA",
                    dates="April 2023",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyData Seattle 2023",
                        url="https://seattle2023.pydata.org/cfp/talk/K8KV8M/",
                        show_icon=True,
                    ),
                    caption=Listed in the inaugural Edge 50, naming the world's top 50 influencers in edge computing,
                    location="Seattle, WA",
                    dates="April 2023",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyData Seattle 2023",
                        url="https://seattle2023.pydata.org/cfp/talk/K8KV8M/",
                        show_icon=True,
                    ),
                    caption=Named best-performing CEO in the world by the Harvard Business Review,
                    location="Seattle, WA",
                    dates="April 2023",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyData Seattle 2023",
                        url="https://seattle2023.pydata.org/cfp/talk/K8KV8M/",
                        show_icon=True,
                    ),
                    caption=Named "Supplier CEO of the year" by Automotive News Europe Eurostars,
                    location="Seattle, WA",
                    dates="April 2023",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyData Seattle 2023",
                        url="https://seattle2023.pydata.org/cfp/talk/K8KV8M/",
                        show_icon=True,
                    ),
                    caption=Received honorary doctorate from National Taiwan University,
                    location="Seattle, WA",
                    dates="April 2023",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyData Seattle 2023",
                        url="https://seattle2023.pydata.org/cfp/talk/K8KV8M/",
                        show_icon=True,
                    ),
                    caption=Received the Robert N. Noyce Award from the Semiconductor Industry Association (SIA), the industry’s highest honor,
                    location="Seattle, WA",
                    dates="April 2023",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyData Seattle 2023",
                        url="https://seattle2023.pydata.org/cfp/talk/K8KV8M/",
                        show_icon=True,
                    ),
                    caption=Was included in the Time 100, Time's annual list of the world's 100 most influential people,
                    location="Seattle, WA",
                    dates="April 2023",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyData Seattle 2023",
                        url="https://seattle2023.pydata.org/cfp/talk/K8KV8M/",
                        show_icon=True,
                    ),
                    caption=Elected to the National Academy of Engineering "for high-powered graphics processing units, fueling the artificial intelligence revolution,
                    location="Seattle, WA",
                    dates="April 2023",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyData Seattle 2023",
                        url="https://seattle2023.pydata.org/cfp/talk/K8KV8M/",
                        show_icon=True,
                    ),
                    caption=recognized as A1 honoree by Gold House,
                    location="Seattle, WA",
                    dates="April 2023",
                ),
            ],
            ],
            ],
            ],
            ],
            ],
            ],
            ],
            ],
            ],
        ),
        Section(
            title="Volunteering",
            entries=[
                SectionEntry(
                    title=LinkText(
                        "ASHA Chennai", url="https://chennai.ashanet.org/", show_icon=True
                    ),
                    caption="Spoken English Teacher",
                    location="Remote",
                    dates="December 2020 - March 2022",
                    description=BulletedList(
                        [
                            "Created a curriculum with story-telling, skits, and friendly debates to provide disadvantaged children isolated in quarantine a fun way to learn spoken English.",
                        ]
                    ),
                )
            ],
        ),
        Section(
            title="Education",
            entries=[
                SectionEntry(
                    title="Oregon State University",
                    location="Corvallis, Oregon",
                    dates="August 1980 - May 1984",
                    description=ItalicsText(
                        "Undergrated in Electrical engineering"
                    ),
                ),
                SectionEntry(
                    title="Stanford University",
                    location="Redwood City, California",
                    dates="August 1984 - May 1992",
                    description=ItalicsText(
                        "Master's degree in electrical engineering"
                    ),
                )
            ],
        ),
        Section(
            title="Skills",
            entries=[
                SectionEntry(
                    description=BulletedList(
                        [
                            ConcatText(
                                UnderlinedText("Languages:"),
                                " Python, Golang, C/C++, JavaScript, C#, Powershell, Zig",
                            ),
                            ConcatText(
                                UnderlinedText("Tools:"),
                                " Kubernetes, PostgreSQL, Linux, Windows, Azure Service Fabric, Distributed Databases, Storage Engines, Docker",
                            ),
                        ]
                    )
                ),
            ],
        ),
    ]
)

if __name__ == "__main__":
    resume.cli_main()
