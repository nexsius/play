from lxml import etree

def checkPackerVer(xml):
    ns = {'xmlns': 'http://maven.apache.org/POM/4.0.0'}
    root = etree.parse(xml)

    plugins = root.findall(".//xmlns:plugin", ns)

    for plugin in plugins:
        artifactId = plugin.find("xmlns:artifactId", ns)
        version = plugin.find("xmlns:version", ns)

        if artifactId.text == "packer" and float(version.text) < 2.0:
            version.text = "2.1"

    modules = root.findall(".//xmlns:modules", ns)

    for module in modules:
        module.remove(module.find("xmlns:core", ns))
    root.write("modules.xml")

if __name__ == "__main__":
    checkPackerVer("modules.xml")
