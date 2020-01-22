#  Copyright (c) 2015 - 2020, Intel Corporation. All rights reserved.<BR>
    def __init__(self, email, description):
        if description is None:
            self.error('Email description is missing!')
            return
        self.description = "'" + description + "'"
            print('The ' + self.description + ' email address is not valid:')
        if ' via Groups.Io' in name and mo.group(3).endswith('@groups.io'):
            self.error("Email rewritten by lists DMARC / DKIM / SPF: " +
                       email)

        print (subject)

            EmailAddressCheck(s[3], sig)
    cve_re = re.compile('CVE-[0-9]{4}-[0-9]{5}[^0-9]')

        if count >= 1 and re.search(self.cve_re, lines[0]):
            #
            # If CVE-xxxx-xxxxx is present in subject line, then limit length of
            # subject line to 92 characters
            #
            if len(lines[0].rstrip()) >= 93:
                self.error(
                    'First line of commit message (subject line) is too long (%d >= 93).' %
                    (len(lines[0].rstrip()))
                    )
        else:
            #
            # If CVE-xxxx-xxxxx is not present in subject line, then limit
            # length of subject line to 75 characters
            #
            if len(lines[0].rstrip()) >= 76:
                self.error(
                    'First line of commit message (subject line) is too long (%d >= 76).' %
                    (len(lines[0].rstrip()))
                    )
                #
                # Print a warning if body line is longer than 75 characters
                #
                print(
                    'WARNING - Line %d of commit message is too long (%d >= 76).' %
                    (i + 1, len(lines[i]))
                    )
                print(lines[i])
                self.force_crlf = True
                self.force_notabs = True
                if self.filename.endswith('.sh'):
                    #
                    # Do not enforce CR/LF line endings for linux shell scripts.
                    #
                    self.force_crlf = False
                if self.filename == '.gitmodules':
                    #
                    # .gitmodules is updated by git and uses tabs and LF line
                    # endings.  Do not enforce no tabs and do not enforce
                    # CR/LF line endings.
                    #
                    self.force_crlf = False
                    self.force_notabs = False
            elif line.startswith('new file mode 160000'):
                #
                # New submodule.  Do not enforce CR/LF line endings
                #
                self.force_crlf = False
        if self.force_notabs and '\t' in line:
        email_check = EmailAddressCheck(self.author_email, 'Author')
        email_ok = email_check.ok

        self.ok = email_ok and msg_ok and diff_ok
        #
        # Parse subject line from email header.  The subject line may be
        # composed of multiple parts with different encodings.  Decode and
        # combine all the parts to produce a single string with the contents of
        # the decoded subject line.
        #
        parts = email.header.decode_header(pmail.get('subject'))
        subject = ''
        for (part, encoding) in parts:
            if encoding:
                part = part.decode(encoding)
            else:
                try:
                    part = part.decode()
                except:
                    pass
            subject = subject + part
        self.commit_subject = subject.replace('\r\n', '')
        self.author_email = pmail['from']

        return self.run_git('show', '--pretty=email', '--no-textconv',
                            '--no-use-mailmap', commit)
        return self.run_git('show', '--pretty=%cn <%ce>', '--no-patch',
                            '--no-use-mailmap', commit)