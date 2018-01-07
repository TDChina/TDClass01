import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

Rectangle {
    id: root
    width: 640; height: 100
    color: "darkgrey"

    SwipeView {
        id: swipeView
        anchors.fill: parent

        Page {
            RowLayout {
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.topMargin: 20
                anchors.centerIn: parent

                TextField {
                    id: textInput
                    placeholderText: qsTr("请输入一个大于1的整数")
                }

                Button {
                    id: button1
                    text: qsTr("计算")
                    onClicked: {
                        swipeView.currentIndex = 1
                        txt.text = primeFactor.analyze(textInput.text)
                    }
                }
            }
        }

        Page {
            Text {
                id: txt
                text: "..."
                font.pixelSize: 30
                anchors.centerIn: parent
            }
            MouseArea {
                id: mouse_area
                anchors.fill: parent
                onClicked: {
                    swipeView.currentIndex = 0
                }
            }
        }
    }
}