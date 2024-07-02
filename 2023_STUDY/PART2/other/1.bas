Sub HighlightContent()
    Dim para As Paragraph
    Dim sContent As String
    Dim bHighlight As Boolean
    Dim iStart As Integer, iEnd As Integer
    Dim hasOparam As Boolean
    Dim oParamContent As String
    Dim A As String
    Dim B As Boolean
    Dim Color As Variant

    Dim searchText As String
    Dim range As range

    Color = wdYellow

    For Each para In ActiveDocument.Paragraphs
        sContent = para.range.Text

        ' ��ɫ
        If InStr(sContent, "<!--") > 0 Then
            Color = wdGreen
        End If
        If InStr(sContent, "-->") > 0 Then
            Color = wdYellow
        End If

        ' ����Ƿ�Ϊ<td>��ǩ
        If InStr(sContent, "<td") > 0 And InStr(sContent, "</td>") > 0 Then
            bHighlight = True ' Ĭ�ϸ���
            para.range.HighlightColorIndex = Color

            ' ����Ƿ���&nbsp;����Ϊ��
            If InStr(sContent, "&nbsp;") > 0 Or Trim(StripTags(sContent)) = vbCr Or Trim(StripTags(sContent)) = "" Then
                bHighlight = False
                para.range.HighlightColorIndex = wdNoHighlight
            End If
            If bHighlight = True Then
                Set range = para.range
                searchText = Trim(StripTags(sContent))
                With range.Find
                    .Text = searchText
                    .Format = True
                    .MatchCase = True
                    .MatchWholeWord = False
                    .Wrap = wdFindContinue
                    .Execute
                    range.HighlightColorIndex = wdRed
                    Set range = ActiveDocument.range(Start:=range.End, End:=ActiveDocument.Content.End)
                End With
            End If



            ' ����Ƿ�����ض��ı�ǩ
            ' If InStr(sContent, "<dsp:valueof bean=") > 0 Or _
            InStr(sContent, "<dsp:importbean") > 0 Or _
               InStr(sContent, "<dsp:param") > 0 Or _
               InStr(sContent, "<dsp:getvalueof") > 0 Then
                ' bHighlight = False
            ' End If
            
        Else
            '            bHighlight = False
            para.range.HighlightColorIndex = wdNoHighlight
        End If

        ' ����Ƿ���<oparam>��ǩ
        If InStr(sContent, "<dsp:oparam") > 0 Then
            bHighlight = True
            para.range.HighlightColorIndex = Color
            A = Trim(StripTags(sContent))

            ' ����Ƿ���&nbsp;����Ϊ��
            If InStr(sContent, "&nbsp;") > 0 Or Trim(StripTags(sContent)) = vbCr Or Trim(StripTags(sContent)) = "" Then
                bHighlight = False
                para.range.HighlightColorIndex = wdNoHighlight
            End If

            If bHighlight = True Then
                Set range = para.range
                searchText = Trim(StripTags(sContent))
                With range.Find
                    .Text = searchText
                    .Format = True
                    .MatchCase = True
                    .MatchWholeWord = False
                    .Wrap = wdFindContinue
                    .Execute
                    range.HighlightColorIndex = wdRed
                    Set range = ActiveDocument.range(Start:=range.End, End:=ActiveDocument.Content.End)
                End With
            End If
            ' ��ȡ<oparam>��ǩ����
            ' iStart = InStr(sContent, "<dsp:oparam")
            ' iEnd = InStr(iStart, sContent, "</dsp:oparam>")
            ' oParamContent = Mid(sContent, iStart, iEnd - iStart + Len("</dsp:oparam>"))

            ' If Trim(StripTags(oParamContent)) <> "" Then
            ' bHighlight = True
            ' End If

        End If

        ' Ӧ�ø���
        '        If bHighlight Then
        '            para.range.HighlightColorIndex = Color
        '        Else
        '            para.range.HighlightColorIndex = wdNoHighlight
        '        End If

    Next
End Sub

Function StripTags(ByVal html As String) As String
    Dim objRegExp As New RegExp
    objRegExp.IgnoreCase = True
    objRegExp.Global = True
    objRegExp.Pattern = "<[^>]*>"
    html = Replace(html, "<br />", "$")
    StripTags = objRegExp.Replace(html, "")
    StripTags = Replace(StripTags, vbCr, "")
    StripTags = Replace(StripTags, vbLf, "")
    StripTags = Replace(StripTags, vbTab, "")
    StripTags = Replace(StripTags, "$", "<br />")
End Function

